from django.urls import path

from accounts.views import (AccountsListView, AccountDetailView, SavedAccountsCreateDeleteView, SavedAccountsListView)

urlpatterns = [

    path('accounts/', AccountsListView.as_view(), name='show-list-of-accounts'),
    path('accounts/<slug:slug>/', AccountDetailView.as_view(), name='show-exact-account'),

    # Saved accounts
    path('saved-account/<int:account_id>/', SavedAccountsCreateDeleteView.as_view(), name='saved-account'),
    path('saved-accounts/', SavedAccountsListView.as_view(), name='show_all_saved-accounts')
]