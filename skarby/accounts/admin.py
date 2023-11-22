from django.contrib import admin
from django.utils.safestring import mark_safe

from accounts.models import Account, Photos, Category


class PhotoInline(admin.TabularInline):
    model = Photos
    extra = 10


class AccountAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'show_avatar', 'is_published')
    readonly_fields = ['show_avatar']
    inlines = [PhotoInline]
    list_per_page = 5
    search_fields = ['name']
    save_on_top = True

    @admin.display(description='Фота')
    def show_avatar(self, account: Account):
        return mark_safe(f"<img src='{account.avatar.url}' width=150")


admin.site.register(Account, AccountAdmin)
admin.site.register(Photos)
admin.site.register(Category)


