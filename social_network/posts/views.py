from django.shortcuts import render, get_object_or_404


from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly


from .models import Post
from posts.serializers import PostSerializer, PostDetailSerializer, PostlikeSerializer
from .permissions import IsAuthorOrReadOnly

class PostList(generics.ListCreateAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostDetailSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly,]

    def get_object(self, **kwargs):
        return get_object_or_404(Post, pk=self.kwargs.get('post_id'))


class LikeListCreate(generics.CreateAPIView):

    def get(self,request,pk):#function to get total number of likes to particular post
        post = Post.objects.filter(pk=pk) # find which post's likes are to be extracted
        like_count = post.likepost.count()# counts total user likes ,besides my code is wrong
        serializer = PostlikeSerializer(like_count,many=True)
        return Response(serializer.data)

    def post(self,request,pk):#function to add likes to post
        # how do I check if user is already liked the post ?
        likeusers = request.user
        likepost = Post.objects.filter(pk=pk)
        serializer = PostlikeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(likeusers,likepost)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)