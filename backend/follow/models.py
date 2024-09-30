from django.db import models

from user.models import User


class Follow(models.Model):
    follower = models.ForeignKey(
    User, 
    related_name='following_set', 
    on_delete=models.CASCADE
    )

    following = models.ForeignKey(
    User, 
    related_name='follower_set', 
    on_delete=models.CASCADE
    )
    
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('follower', 'following')

    def __str__(self):
        return f"{self.follower.username} follows {self.following.username}"
