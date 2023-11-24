from django.urls import path

from accounts.views import AccountsListView, AccountDetailView, SaveAccountView, SavedAccountsListView

urlpatterns = [

    path('accounts/', AccountsListView.as_view()),
    path('accounts/<slug:account_slug>/', AccountDetailView.as_view()),

    path('save-account/<int:account_id>/', SaveAccountView.as_view(), name='save-account'),
    path('saved-accounts/', SavedAccountsListView.as_view(), name='show_saved-accounts'),
]