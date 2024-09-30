from rest_framework import serializers

from .models import Story, Like, Comment

from user.serializers import UserSerializer


class StorySerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    likes_count = serializers.IntegerField(source='likeCount', read_only=True)
    comments_count = serializers.IntegerField(source='commentCount', read_only=True)

    class Meta:
        model = Story
        fields = ['id', 'user', 'image', 'created_at', 'expired_at', 'likes_count', 'comments_count']


class LikeSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Like
        fields = ['id', 'user', 'story']


class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'user', 'story', 'content', 'created_at']
