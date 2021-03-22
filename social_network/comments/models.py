from django.db import models
from django.contrib.auth.models import User

from posts.models import Post

class Review(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='User')
    text = models.TextField()
    post = models.ForeignKey(Post, verbose_name='rewiew_post', on_delete=models.CASCADE, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    reply_to = models.ForeignKey('self', on_delete=models.SET_NULL, related_name='child', null=True, blank=True)

    class Meta:
        ordering = ['created',]

    
    def __str__(self):
        return f'Review by {self.user} on {self.post}'