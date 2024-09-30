from django.contrib import admin

from .models import Story, Like, Comment


admin.site.register(Story)

admin.site.register(Like)

admin.site.register(Comment)
