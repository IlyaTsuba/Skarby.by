from rest_framework.serializers import ModelSerializer

from articles.models import Article


class ArticleSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = ('title', 'content', 'time_create', 'article_slug', 'article_category', 'account', 'is_published')