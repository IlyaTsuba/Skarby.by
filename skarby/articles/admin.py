from django.contrib import admin
from articles.models import Article, ArticlePhotos, ArticleCategory


class ArticleCategoryAdmin(admin.ModelAdmin):
    model = ArticleCategory
    prepopulated_fields = {'slug': ('name',)}


class ArticlePhotoInline(admin.TabularInline):
    model = ArticlePhotos
    extra = 10


class ArticleAdmin(admin.ModelAdmin):
    model = Article
    list_display = ('id', 'title', 'time_create', 'slug', 'article_category', 'is_published')
    inlines = [ArticlePhotoInline]
    list_per_page = 5
    search_fields = ['title']
    save_on_top = True
    list_display_links = 'id', 'title'
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Article, ArticleAdmin)
admin.site.register(ArticlePhotos)
admin.site.register(ArticleCategory, ArticleCategoryAdmin)
