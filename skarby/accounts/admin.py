from django.contrib import admin
from django.utils.safestring import mark_safe

from accounts.models import Account, Photos, Category


class CategoryAdmin(admin.ModelAdmin):
    model = Category
    prepopulated_fields = {'category_slug': ('name',)}


class PhotoInline(admin.TabularInline):
    model = Photos
    extra = 10


class AccountAdmin(admin.ModelAdmin):
    model = Account
    list_display = ('id', 'name', 'category', 'show_avatar', 'is_published')
    readonly_fields = ['show_avatar']
    inlines = [PhotoInline]
    list_per_page = 5
    search_fields = ['name']
    save_on_top = True
    list_display_links = 'id', 'name'
    prepopulated_fields = {'account_slug': ('name',)}

    # Show same size avatars in admin panel
    @admin.display(description='Аватар')
    def show_avatar(self, account: Account):
        return mark_safe(f"<img src='{account.avatar.url}' width=150")


admin.site.register(Account, AccountAdmin)
admin.site.register(Photos)
admin.site.register(Category, CategoryAdmin)


