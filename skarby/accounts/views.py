from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView

from accounts.models import Account, SavedAccount
from accounts.serializers import AccountSerializer, SavedAccountSerializer


class AccountsListView(ListAPIView):
    """
    This view is to show all published posts.
    """
    queryset = Account.objects.filter(is_published=Account.Status.PUBLISHED)  # Show only accepted to publish accounts
    serializer_class = AccountSerializer


class AccountDetailView(APIView):
    def get(self, request, account_slug):
        account = get_object_or_404(Account, account_slug=account_slug)

        serializer = AccountSerializer(account)

        return Response(serializer.data)


# Save account functionality
class SaveAccountView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, account_id):
        account = get_object_or_404(Account, id=account_id)
        user = self.request.user

        saved_account, created = SavedAccount.objects.get_or_create(user=user, account=account)

        if created:
            return Response({'message': 'Account saved successfully.'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': 'Account already saved.'}, status=status.HTTP_200_OK)


class SavedAccountsListView(APIView):
    permission_classes = [IsAuthenticated, ]

    def get(self, request):
        user = self.request.user
        saved_accounts = SavedAccount.objects.filter(user=user)
        serializer = SavedAccountSerializer(saved_accounts, many=True)
        return Response(serializer.data)