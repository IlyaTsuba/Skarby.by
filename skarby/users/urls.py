from django.urls import path, include
from users.views import ActivateUser, PasswordResetView, TestView

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('accounts/activate/<uid>/<token>/', ActivateUser.as_view({'get': 'activation'}), name='activation'),
    path('accounts/password/reset/confirm/<uid>/<token>/', PasswordResetView.as_view(), name='reset_password'),
    path('', TestView.as_view())
]