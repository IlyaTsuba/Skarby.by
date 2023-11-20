from django.contrib import admin
from accounts.models import Account, Photos, Category


class PhotoInline(admin.TabularInline):
    model = Photos
    extra = 10


class AccountAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    inlines = [PhotoInline]
    list_per_page = 5
    search_fields = ['name']


admin.site.register(Account, AccountAdmin)
admin.site.register(Photos)
admin.site.register(Category)


