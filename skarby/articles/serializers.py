from rest_framework.serializers import ModelSerializer, SerializerMethodField

from articles.models import Article, ArticlePhotos, ArticleLikes


class PhotosSerializer(ModelSerializer):
    class Meta:
        model = ArticlePhotos
        fields = ('photo',)


class ArticleSerializer(ModelSerializer):
    photo = PhotosSerializer(many=True, read_only=True, source='article_photos')
    likes_count = SerializerMethodField()
    category = SerializerMethodField()

    class Meta:
        model = Article
        fields = ('title', 'content', 'time_create', 'slug', 'category',
                  'account', 'is_published', 'photo', 'likes_count')

    def get_likes_count(self, article):
        likes_count = ArticleLikes.objects.filter(article_id=article.id).count()
        return likes_count

    def get_category(self, account):
        return account.category.name
