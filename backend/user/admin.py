from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, Profile, OTP


class Admin(UserAdmin):
    list_display = ('pk', 'phone', 'is_superuser')
    filter_horizontal = ()
    list_filter = ('is_superuser', )
    fieldsets = ()
    ordering = ('pk', )


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone')


admin.site.register(User, Admin)

admin.site.register(Profile, ProfileAdmin)

admin.site.register(OTP)
