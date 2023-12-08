from django.shortcuts import render, get_object_or_404, get_list_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from articles.models import Article
from accounts.models import Account
from mainpage.serializers import LastArticlesSerializer, LastAccountsSerializer


class LastArticlesView(APIView):
    def get(self, request):
        last_two_articles = get_list_or_404(Article.objects.filter
                                            (is_published=Article.Status.PUBLISHED).order_by('-id')[:2])
        serializer = LastArticlesSerializer(last_two_articles, many=True)
        return Response(serializer.data)


class LastAccountsView(APIView):
    def get(self, request):
        last_four_accounts = get_list_or_404(Account.objects.filter
                                             (is_published=Article.Status.PUBLISHED).order_by('-id')[:4])
        serializer = LastAccountsSerializer(last_four_accounts, many=True)
        return Response(serializer.data)
