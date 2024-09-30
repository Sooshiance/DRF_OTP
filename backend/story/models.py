from django.db import models

from user.models import User


class Story(models.Model):
    user       = models.ForeignKey(User, on_delete=models.CASCADE, related_name='stories')
    image      = models.ImageField(upload_to='stories/')
    created_at = models.DateTimeField(auto_now_add=True)
    expired_at = models.DateTimeField()

    def __str__(self):
        return f"{self.user.username}'s story"
    
    def likeCount(self):
        return self.likes.count()
    
    def commentCount(self):
        return self.comments.count()
    
    class Meta:
        verbose_name = 'Story'
        verbose_name_plural = 'Stories'


class Like(models.Model):
    user  = models.ForeignKey(User, on_delete=models.CASCADE)
    story = models.ForeignKey(Story, on_delete=models.CASCADE, related_name='likes')

    def __str__(self):
        return f"{self.user} {self.story}"


class Comment(models.Model):
    user       = models.ForeignKey(User, on_delete=models.CASCADE)
    story      = models.ForeignKey(Story, on_delete=models.CASCADE, related_name='comments')
    content    = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} {self.story}"
