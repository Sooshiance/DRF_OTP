from rest_framework import serializers

from .models import Post, Like, Comment

from user.serializers import UserSerializer


class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    likes_count = serializers.IntegerField(source='likeCount', read_only=True)
    comments_count = serializers.IntegerField(source='commentCount', read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'image', 'caption', 'created_at', 'updated_at', 'location', 'user', 'likes_count', 'comments_count']


class LikeSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Like
        fields = ['id', 'user', 'post']


class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'user', 'post', 'content', 'created_at']
