from django.contrib import admin
from articles.models import Article, ArticlePhotos, ArticleCategory


class ArticleCategoryAdmin(admin.ModelAdmin):
    model = ArticleCategory
    prepopulated_fields = {'article_category_slug': ('name',)}


class ArticlePhotoInline(admin.TabularInline):
    model = ArticlePhotos
    extra = 10


class ArticleAdmin(admin.ModelAdmin):
    model = Article
    list_display = ('id', 'title', 'time_create', 'article_slug', 'article_category', 'is_published')
    # readonly_fields = ['show_avatar']
    inlines = [ArticlePhotoInline]
    list_per_page = 5
    search_fields = ['title']
    save_on_top = True
    list_display_links = 'id', 'title'
    prepopulated_fields = {'article_slug': ('title',)}


admin.site.register(Article, ArticleAdmin)
admin.site.register(ArticlePhotos)
admin.site.register(ArticleCategory, ArticleCategoryAdmin)
