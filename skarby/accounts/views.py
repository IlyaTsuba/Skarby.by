from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView

from accounts.models import Account
from accounts.serializers import AccountSerializer


class AccountsListView(ListAPIView):
    queryset = Account.objects.filter(is_published=Account.Status.PUBLISHED)  # Show only accepted to publish accounts
    serializer_class = AccountSerializer


