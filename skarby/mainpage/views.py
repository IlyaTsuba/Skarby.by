from django.shortcuts import get_list_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.serializers import AccountSerializer, AccountListSerializer
from articles.models import Article
from accounts.models import Account
from articles.serializers import ArticleSerializer


class LastArticlesView(APIView):
    def get(self, request):
        last_two_articles = get_list_or_404(Article.objects.filter
                                            (is_published=Article.Status.PUBLISHED).order_by('-id')[:2])
        serializer = ArticleSerializer(last_two_articles, many=True)
        return Response(serializer.data)


class LastAccountsView(APIView):
    def get(self, request):
        last_four_accounts = get_list_or_404(Account.objects.filter
                                             (is_published=Article.Status.PUBLISHED).order_by('-id')[:4])
        serializer = AccountListSerializer(last_four_accounts, many=True)
        return Response(serializer.data)
