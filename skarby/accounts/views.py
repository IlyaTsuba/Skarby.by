from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView

from accounts.models import Account
from accounts.serializers import AccountSerializer


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

