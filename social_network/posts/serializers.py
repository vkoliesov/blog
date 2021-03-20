from django.contrib.auth.models import User

from rest_framework import serializers

from .models import Post

class PostDetailSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='autor.username')
        
    class Meta:
        model = Post
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    
    author = serializers.ReadOnlyField(source='autor.username')
    
    class Meta:
        model = Post
        fields = ['id', 'author', 'title','text', ]
