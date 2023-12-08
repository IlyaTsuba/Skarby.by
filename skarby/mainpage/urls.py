from django.urls import path

from mainpage.views import LastArticlesView, LastAccountsView

urlpatterns = [
    path('last-articles/', LastArticlesView.as_view(), name='last-articles'),
    path('last-accounts/', LastAccountsView.as_view(), name='last-accounts')
]