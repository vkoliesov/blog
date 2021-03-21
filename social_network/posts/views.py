from collections import Counter
from itertools import groupby


from django.shortcuts import render, get_object_or_404
from django_filters import rest_framework as filters

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly


from .models import Post, PostLike
from posts.serializers import PostSerializer, PostDetailSerializer, PostlikeSerializer
from .permissions import IsAuthorOrReadOnly
from .filters import DateRangeFilterSet


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


class AnalyticView(generics.GenericAPIView):
    queryset = PostLike.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = DateRangeFilterSet

    def get(self, request, format=None):
        queryset = self.get_queryset()
        filtered_queryset = self.filter_queryset(queryset)

        # Queryset needs to be ordered by date for groupby to work correctly
        ordered_queryset = filtered_queryset.order_by('date')
        likes_by_date = groupby(ordered_queryset,
                                lambda like: like.date.strftime("%Y-%m-%d"))

        analytics = []
        for date, likes in likes_by_date:
            count = Counter(like.like for like in likes)
            analytics.append(
                {
                    'date': date,
                    'total_likes': count['like'],
                    'total_dislikes': count['dislike'],

                }
            )

        return Response(analytics)  