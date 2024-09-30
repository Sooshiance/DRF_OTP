from django.contrib import admin

from .models import Follow


class FollowAdmin(admin.ModelAdmin):
    list_display = ['follower', 'following']


admin.site.register(Follow, FollowAdmin)
