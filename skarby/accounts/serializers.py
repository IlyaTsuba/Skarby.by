from rest_framework.serializers import ModelSerializer, SerializerMethodField

from accounts.models import Account, SavedAccount, Photos, AccountLikes


class PhotosSerializer(ModelSerializer):
    class Meta:
        model = Photos
        fields = ('photo',)
        ref_name = 'PhotosSerializerModel'


class AccountListSerializer(ModelSerializer):
    photo = PhotosSerializer(many=True, read_only=True, source='account_list')

    class Meta:
        model = Account
        fields = ('slug', 'name', 'description', 'instagram', 'telegram', 'avatar', 'category', 'photo')


class AccountSerializer(ModelSerializer):
    photo = PhotosSerializer(many=True, read_only=True, source='account_photos')
    likes_count = SerializerMethodField()

    class Meta:
        model = Account
        fields = ('slug', 'name', 'description', 'instagram', 'telegram', 'avatar', 'category', 'photo', 'likes_count',
                  'is_published')

    def get_likes_count(self, account):
        likes_count = AccountLikes.objects.filter(account_id=account.id).count()
        return likes_count


class SavedAccountSerializer(ModelSerializer):
    class Meta:
        model = SavedAccount
        fields = ('user', 'account', 'created_at')
