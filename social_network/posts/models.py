from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    author = models.ForeignKey('auth.User', null=True, blank=False, on_delete=models.SET_NULL)
    title = models.CharField(max_length=255)
    text = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

class PostLike(models.Model):
    LIKE = (
        ('like', 'like'),
        ('dislike', 'dislike')
    )

    likes_user = models.ForeignKey('auth.User', blank=True, related_name='post_likes', on_delete=models.CASCADE, default=None)
    likes_post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    like = models.CharField(max_length=255, choices=LIKE, default=0)
    date = models.DateField(auto_now=True)

