from django.urls import path
from django.contrib.auth import views as auth_views

from . import views


urlpatterns = [
    path('', views.UserList.as_view(), name='list_users'),
    path('<int:user_id>/', views.UserDetail.as_view(), name='user_detail'),
    path('<int:user_id>/update/', views.UserUpdate.as_view(), name='user_update'),
    path('profiles/', views.UserProfileList.as_view(), name='profile_list'),
    path('profiles/<int:user_id>/', views.UserProfileDetail.as_view(), name='profile_detail'),
    path('signup/', views.SignupAPI.as_view(), name='signup'),
    # path('login/',auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    # path('signup/', views.UserSignupView.as_view(), name='signup'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),

]