from django.urls import path

from accounts.views import AccountsListView, AccountDetailView

urlpatterns = [

    path('accounts/', AccountsListView.as_view()),
    path('accounts/<slug:account_slug>/', AccountDetailView.as_view())
]