from django.contrib import admin
from accounts.models import Account, Photos


class PhotoInline(admin.TabularInline):
    model = Photos
    extra = 1


class AccountAdmin(admin.ModelAdmin):
    inlines = [PhotoInline]


admin.site.register(Account, AccountAdmin)
admin.site.register(Photos)