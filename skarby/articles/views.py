from django.shortcuts import render, get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from rest_framework.response import Response
from articles.models import Article
from rest_framework.generics import ListAPIView

from articles.serializers import ArticleSerializer


# class ArticleListPagination(PageNumberPagination):
#     page_size = 2
#     page_size_query_param = 'page_size'
#     max_page_size = 10


class ArticlesListView(ListAPIView):
    """
    This view is to show all published articles.
    """
    queryset = Article.objects.filter(is_published=Article.Status.PUBLISHED)  # Show only accepted to publish articles
    serializer_class = ArticleSerializer
    filter_backends = (DjangoFilterBackend,)
    # pagination_class = ArticleListPagination


class ArticleDetailView(APIView):
    """
    This view is to show exact Account details
    """

    def get(self, request, slug):
        article = get_object_or_404(Article, slug=slug, is_published=Article.Status.PUBLISHED)
        serializer = ArticleSerializer(article)

        return Response(serializer.data)