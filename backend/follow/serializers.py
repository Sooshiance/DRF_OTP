from rest_framework import serializers

from .models import Follow
from user.models import User


class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follow
        exclude = ['created_at']
    
    def validate(self, attrs):

        # TODO: Check follower and following
        follower = attrs.get('follower')
        following = attrs.get('following')

        if follower == following:
            raise serializers.ValidationError("Follower and following cannot be the same user.")

        if not User.objects.filter(pk=follower.id).exists():
            raise serializers.ValidationError("Follower user does not exist.")

        if not User.objects.filter(pk=following.id).exists():
            raise serializers.ValidationError("Following user does not exist.")
        
        if following.is_private:
            raise serializers.ValidationError("You cannot follow this user because his account is private.")

        return attrs
