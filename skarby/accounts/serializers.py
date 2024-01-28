from django.contrib.auth.models import AnonymousUser
from rest_framework.serializers import ModelSerializer, SerializerMethodField

from accounts.models import Account, SavedAccount, Photos, AccountLikes, SocialMedia


class PhotosSerializer(ModelSerializer):
    class Meta:
        model = Photos
        fields = ('photo',)
        ref_name = 'PhotosSerializerModel'


class SocialMediaSerializer(ModelSerializer):
    class Meta:
        model = SocialMedia
        fields = ('instagram', 'telegram', 'youtube', 'tiktok', 'site')


class AccountListSerializer(ModelSerializer):
    category = SerializerMethodField()
    avatar = SerializerMethodField()

    class Meta:
        model = Account
        fields = ('slug', 'name', 'description', 'avatar', 'category')

    def get_category(self, account):
        return account.category.name

    def get_avatar(self, account):
        return account.avatar.url


class AccountSerializer(ModelSerializer):
    photo = PhotosSerializer(many=True, read_only=True, source='account_photos')
    likes_count = SerializerMethodField()
    category = SerializerMethodField()
    is_liked = SerializerMethodField()
    social_media = SocialMediaSerializer(many=True, source='account_social_media', read_only=True)

    class Meta:
        model = Account
        fields = ('slug', 'name', 'description', 'avatar', 'category', 'photo', 'likes_count',
                  'is_published', 'is_liked', 'social_media')

    # def get_is_liked(self, account):
    #     user = self.context['request'].user
    #     if not isinstance(user, AnonymousUser):
    #         return AccountLikes.objects.filter(user_id=user.id, account_id=account.id).exists()
    def get_is_liked(self, account):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            user = request.user
            return AccountLikes.objects.filter(user=user, account=account).exists()
        return False

    def get_likes_count(self, account):
        likes_count = AccountLikes.objects.filter(account_id=account.id).count()
        return likes_count

    def get_category(self, account):
        return account.category.name


class SavedAccountSerializer(ModelSerializer):
    class Meta:
        model = SavedAccount
        fields = ('user', 'account', 'created_at')
