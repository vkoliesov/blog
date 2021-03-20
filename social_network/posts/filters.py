import django_filters

from .models import Post

class LikeItemFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(name='post__title')
    likes = django_filters.CharFilter(name='post__total_likes')
    start_date = django_filters.DateFilter(name='date',lookup_type=('lt'),) 
    end_date = django_filters.DateFilter(name='date',lookup_type=('gt'))
    date = django_filters.DateRangeFilter()

    class Meta:
        model = Post
        fields = ['title', 'likes_date_from', 'likes_date_to']