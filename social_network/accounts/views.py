from django.shortcuts import get_object_or_404, render, Http404
from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth.forms  import UserCreationForm
from django.urls import reverse_lazy

from rest_framework import generics
from rest_framework.response import Response

from accounts.serializers import UserSerializer, UserProfileSerializer, RegisterSerializer
from .models import UserProfile


class UserList(generics.ListCreateAPIView):
    
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer

    def get_object(self, **kwargs):
        return get_object_or_404(User,  pk=self.kwargs.get('user_id'))


# Register API

class SignupAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args,  **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user,    context=self.get_serializer_context()).data,
            "message": "User Created Successfully.  Now perform Login to get your token",
        })

class UserProfileList(generics.ListAPIView):
    
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class UserProfileDetail(generics.RetrieveUpdateAPIView):
    
    serializer_class = UserProfileSerializer
    # permission_classes = [IsUserOrReadOnly, IsAdminUser]

    def get_object(self, **kwargs):
        return get_object_or_404(UserProfile,  pk=self.kwargs.get('user_id'))



# class UserSignupView(generic.CreateView):
#     form_class = UserCreationForm
#     template_name = 'registration/signup.html'
#     success_url = reverse_lazy('login')


# class UserProfileList(generics.ListCreateAPIView):
#     queryset = UserProfile.objects.all()
#     search_fields = ['first_name', 'last_name']
#     serializer_class = UserProfileSerializer

#     def get_search_fields(self, view, request):
#         return request.GET.getlist('search_fields', [])
        