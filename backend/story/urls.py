from django.urls import path

from .views import (
    StoryListCreateView,
    StoryDetailView,
    LikeListCreateView,
    CommentListCreateView,
    CommentDetailView,
)


app_name = "story"

urlpatterns = [
    path('stories/', StoryListCreateView.as_view(), name='story-list-create'),
    path('stories/<int:pk>/', StoryDetailView.as_view(), name='story-detail'),
    path('likes/', LikeListCreateView.as_view(), name='like-list-create'),
    path('comments/', CommentListCreateView.as_view(), name='comment-list-create'),
    path('comments/<int:pk>/', CommentDetailView.as_view(), name='comment-detail'),
]
