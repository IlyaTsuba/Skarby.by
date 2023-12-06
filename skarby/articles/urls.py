from django.urls import path

from articles.views import ArticlesListView, ArticleDetailView

urlpatterns = [

    path('articles/', ArticlesListView.as_view(), name='show-all-articles'),
    path('articles/<slug:slug>/', ArticleDetailView.as_view(), name='show-exact-article'),
]