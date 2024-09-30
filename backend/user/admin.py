from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User, Profile


class UserAdmin(BaseUserAdmin):
    list_display = ['phone', 'email','username']
    filter_horizontal = ()
    list_filter = ('is_superuser', 'is_private')
    fieldsets = ()
    search_fields = ['email']


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user',)


admin.site.register(User, UserAdmin)


admin.site.register(Profile, ProfileAdmin)
