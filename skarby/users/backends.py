from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q


class CustomAuthenticationBackend(ModelBackend):
    """
    This custom backend allows users to log in, using both email and username
    """

    def authenticate(self, request, email=None, password=None, **kwargs):

        UserModel = get_user_model()  # get user model, in our case UserModel = CustomUser

        try:
            user = UserModel.objects.get(Q(email=email) | Q(username=email))
            # identify user using email or username
        except UserModel.DoesNotExist:
            return None

        if user.check_password(password):  # check password
            return user

    def get_user(self, user_id):
        UserModel = get_user_model()

        try:
            return UserModel.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None
