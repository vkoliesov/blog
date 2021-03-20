from django.shortcuts import render, get_object_or_404

from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly


from .models import Post
from posts.serializers import PostSerializer, PostDetailSerializer
from .permissions import IsAuthorOrReadOnly

class PostList(generics.ListCreateAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostDetailSerializer
    permission_classes = [IsAuthorOrReadOnly,]

    def get_object(self, **kwargs):
        return get_object_or_404(Post, pk=self.kwargs.get('post_id'))

