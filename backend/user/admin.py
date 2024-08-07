from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, Profile, OTP
from .forms import UserCreationForm


class Admin(UserAdmin):
    add_form = UserCreationForm
    list_display = ('id', 'phone', 'last_name')
    list_display_links = ['phone', 'id']
    filter_horizontal = ()
    list_filter = []
    search_fields = ['phone', 'fullName']
    ordering = ['id', 'last_name']

    fieldsets = (
    (None, {'fields': ('phone',)}),
    ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
    ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    ('Important dates', {'fields': ('last_login',)}),
    )

    add_fieldsets = (
    (None, {
    'classes': ('wide',),
    'fields': ('phone', 'first_name', 'last_name', 'email'),
    }),
    )


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone')


admin.site.register(User, Admin)

admin.site.register(Profile, ProfileAdmin)

admin.site.register(OTP)
