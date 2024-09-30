from django.urls import path

from .views import (PostListCreateView,
                    PostDetailView,
                    LikeListCreateView,
                    CommentListCreateView,
                    CommentDetailView,)


app_name = "post"

urlpatterns = [
    path('posts/', PostListCreateView.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('likes/', LikeListCreateView.as_view(), name='like-list-create'),
    path('comments/', CommentListCreateView.as_view(), name='comment-list-create'),
    path('comments/<int:pk>/', CommentDetailView.as_view(), name='comment-detail'),
]
