from rest_framework.serializers import ModelSerializer

from accounts.models import Account, SavedAccount


class AccountSerializer(ModelSerializer):
    class Meta:
        model = Account
        fields = ('account_slug', 'name', 'description', 'instagram', 'telegram', 'avatar', 'category')


class SavedAccountSerializer(ModelSerializer):
    class Meta:
        model = SavedAccount
        fields = ('user', 'account', 'created_at')
