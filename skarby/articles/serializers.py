from rest_framework.serializers import ModelSerializer

from articles.models import Article, ArticlePhotos


class PhotosSerializer(ModelSerializer):
    class Meta:
        model = ArticlePhotos
        fields = ('photo',)


class ArticleSerializer(ModelSerializer):
    photo = PhotosSerializer(many=True, read_only=True, source='article_photos')

    class Meta:
        model = Article
        fields = ('title', 'content', 'time_create', 'slug', 'article_category',
                  'account', 'is_published', 'photo')
