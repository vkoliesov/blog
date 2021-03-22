from django.urls import path

from . import views

urlpatterns = [
    
    path('reviews/', views.ReviewListCreate.as_view(), name='review_list'),
    path('reviews/<int:review_id>/', views.ReviewRetrieve.as_view(), name='review_details'),

]