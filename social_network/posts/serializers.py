from django.contrib.auth.models import User

from rest_framework import serializers

from .models import Post, PostLike

class PostlikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostLike
        fields = '__all__'

class PostDetailSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='autor.username')
    likes = PostlikeSerializer(many=True)
        
    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'title', 'likes', 'updated']


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='autor.username')
    likes = PostlikeSerializer(many=True)
    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'text', 'likes']

