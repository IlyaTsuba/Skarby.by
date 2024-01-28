from django.contrib import admin
from django.utils.safestring import mark_safe

from accounts.models import Account, Photos, Category, AccountLikes, SocialMedia


class CategoryAdmin(admin.ModelAdmin):
    model = Category
    prepopulated_fields = {'slug': ('name',)}


class PhotoInline(admin.TabularInline):
    model = Photos
    extra = 10


class SocialMediaInline(admin.TabularInline):
    model = SocialMedia
    extra = 1


class SocialMediaAdmin(admin.ModelAdmin):
    model = SocialMedia
    list_display = ('account', 'instagram', 'telegram', 'youtube', 'tiktok', 'site')


class AccountAdmin(admin.ModelAdmin):
    model = Account
    list_display = ('id', 'name', 'category', 'show_avatar', 'is_published')
    readonly_fields = ['show_avatar']
    inlines = [SocialMediaInline, PhotoInline]
    list_per_page = 5
    search_fields = ['name']
    save_on_top = True
    list_display_links = 'id', 'name'
    prepopulated_fields = {'slug': ('name',)}

    @admin.display(description='Аватар')
    def show_avatar(self, account: Account):
        return mark_safe(f"<img src='{account.avatar.url}' width=150")


admin.site.register(Account, AccountAdmin)
admin.site.register(Photos)
admin.site.register(Category, CategoryAdmin)
admin.site.register(AccountLikes)
admin.site.register(SocialMedia, SocialMediaAdmin)

