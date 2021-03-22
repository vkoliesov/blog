from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Review

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username']


class RecursiveSerializer(serializers.Serializer):

    def to_representation(self, value):
        serializers = self.parent.parent.__class__(value, context=self.context)
        return serializers.data


class ReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    child = RecursiveSerializer(many=True, read_only=True)

    class Meta:
    
        model = Review
        fields = ['user', 'post', 'text', 'created', 'child', 'reply_to']