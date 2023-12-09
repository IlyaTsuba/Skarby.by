from django.shortcuts import render, get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from articles.models import Article, ArticleLikes
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
    queryset = Article.objects.filter(is_published=Article.Status.PUBLISHED).select_related('category')  # Show only accepted to publish articles
    serializer_class = ArticleSerializer
    filter_backends = (DjangoFilterBackend,)
    # pagination_class = ArticleListPagination


class ArticleDetailView(APIView):
    """
    This view is to show exact Account details
    """

    def get(self, request, slug):
        article = get_object_or_404(
            Article.objects.select_related('category'), slug=slug, is_published=Article.Status.PUBLISHED)
        serializer = ArticleSerializer(article)

        return Response(serializer.data)


class ArticleLikeView(APIView):
    permission_classes = [IsAuthenticated, ]

    def post(self, request, slug):
        user = request.user
        article = get_object_or_404(Article, slug=slug)

        liked_account, created = ArticleLikes.objects.get_or_create(user=user, article=article)

        if created:  # True, add like
            return Response({'message': 'Падабаечка!'}, status=status.HTTP_201_CREATED)
        else:  # False, like exists
            return Response({'message': 'Ужо спадабалася!'}, status=status.HTTP_200_OK)

    def delete(self, request, slug):
        user = request.user
        article = get_object_or_404(Article, slug=slug)
        like_to_delete = get_object_or_404(ArticleLikes, user=user, article_id=article.id)
        if like_to_delete:
            like_to_delete.delete()
            return Response({'message': 'Падабаечка выдалена:('}, status=status.HTTP_200_OK)