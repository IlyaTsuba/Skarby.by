from rest_framework.serializers import ModelSerializer

from accounts.models import Account
from articles.models import Article


class LastArticlesSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = ('title', 'content', 'time_create', 'slug', 'article_category',
                  'account', 'is_published')


class LastAccountsSerializer(ModelSerializer):
    class Meta:
        model = Account
        fields = ('slug', 'name', 'description', 'instagram', 'telegram', 'avatar', 'category', 'is_published')