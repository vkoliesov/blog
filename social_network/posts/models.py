from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    author = models.ForeignKey('auth.User', null=True, blank=False, on_delete=models.SET_NULL, related_name='posts')
    title = models.CharField(max_length=255)
    text = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    likes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-updated']