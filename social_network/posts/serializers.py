from rest_framework import serializers

from .models import Post

class PostSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField(read_only=True)

    def get_author(self, obj):
        return str(obj.author.username)
        
    class Meta:
        model = Post
        fields = '__all__'