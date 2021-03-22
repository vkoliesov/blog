from django.shortcuts import get_object_or_404

from rest_framework import generics, filters
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly


from .models import Review
from comments.serializers import ReviewSerializer
from .permissions import IsOwnerOrReadOnly

# Create your views here.


class ReviewListCreate(generics.ListCreateAPIView):
    pagination_class = LimitOffsetPagination
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Review.objects.filter(reply_to=None).order_by('-created')
    serializer_class = ReviewSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['created']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        reply = serializer.data['reply_to']



class ReviewRetrieve(generics.RetrieveUpdateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_object(self):
        return get_object_or_404(Review, pk=self.kwargs.get('review_id'))