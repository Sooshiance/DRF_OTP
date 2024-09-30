from django.shortcuts import get_object_or_404

from rest_framework import generics, permissions

from .models import Follow
from .serializers import FollowSerializer

from user.models import User


class FollowCreateAPIView(generics.CreateAPIView):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        follower = self.request.user
        print(follower)
        following = get_object_or_404(User, email=follower.email)
        serializer.save(follower=follower, following=following)


class FollowDeleteAPIView(generics.DestroyAPIView):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        follower = self.request.user
        following = get_object_or_404(User, email=follower.email)
        return get_object_or_404(Follow, follower=follower, following=following)


class FollowerListAPIView(generics.ListAPIView):
    serializer_class = FollowSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return user.following_set.all()


class FollowingListAPIView(generics.ListAPIView):
    serializer_class = FollowSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        print(f"following set === {user.following_set.all()}")
        return user.follower_set.all()
