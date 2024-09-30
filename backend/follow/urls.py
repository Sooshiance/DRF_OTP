from django.urls import path

from .views import (
    FollowCreateAPIView, 
    FollowDeleteAPIView,
    FollowerListAPIView,
    FollowingListAPIView,
)


app_name = "follow"

urlpatterns = [
    path("create/", FollowCreateAPIView.as_view(), name='create'),
    path("delete/", FollowDeleteAPIView.as_view(), name='delete'),
    path('followers/<int:pk>/', FollowerListAPIView.as_view(), name='follower-list'),
    path('following/<int:pk>/', FollowingListAPIView.as_view(), name='following-list'),
]
