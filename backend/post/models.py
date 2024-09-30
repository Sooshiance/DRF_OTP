from django.db import models

from user.models import User


class Post(models.Model):
    image          = models.ImageField(upload_to='posts/', blank=True, null=True)
    caption        = models.TextField(blank=True, null=True)
    created_at     = models.DateTimeField(auto_now_add=True)
    updated_at     = models.DateTimeField(auto_now=True)
    location       = models.CharField(max_length=100, blank=True, null=True)
    user           = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')

    def likeCount(self):
        return self.likes.count()
    
    def commentCount(self):
        return self.comments.count()

    def __str__(self):
        return f"{self.user.username}'s post"


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')

    def __str__(self):
        return f"{self.user} {self.post}"


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} {self.post}"
