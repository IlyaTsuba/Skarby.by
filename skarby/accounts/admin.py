from django.contrib import admin
from accounts.models import Account, Photos, Category


class PhotoInline(admin.TabularInline):
    model = Photos
    extra = 10


class AccountAdmin(admin.ModelAdmin):
    inlines = [PhotoInline]


admin.site.register(Account, AccountAdmin)
admin.site.register(Photos)
admin.site.register(Category)