from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name='list_posts'),
    path('<int:post_id>/', views.PostDetail.as_view(), name='post_detail'),
    path('<int:post_id>/like/',views.LikeListCreate.as_view(),name = 'post_likes'),


]