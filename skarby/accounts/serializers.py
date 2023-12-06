from rest_framework.serializers import ModelSerializer

from accounts.models import Account, SavedAccount, Photos


class PhotosSerializer(ModelSerializer):
    class Meta:
        model = Photos
        fields = ('photo', )


class AccountSerializer(ModelSerializer):
    photo = PhotosSerializer(many=True, read_only=True, source='account_photos')

    class Meta:
        model = Account
        fields = ('slug', 'name', 'description', 'instagram', 'telegram', 'avatar', 'category', 'photo')


class SavedAccountSerializer(ModelSerializer):
    class Meta:
        model = SavedAccount
        fields = ('user', 'account', 'created_at')
