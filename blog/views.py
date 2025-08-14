from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, AllowAny
from .models import Blog
from .serializers import BlogSerializer

# Create your views here.

def blog(request):
    context ={

    }
    return render(request, 'blog.html' ,context)


class ListCreateBlogApi(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    def get_permissions(self):
        self.permission_classes = [AllowAny]
        if self.request.method == "POST":
            self.permission_classes = [IsAdminUser]    
        return super().get_permissions()
    

class BlogDetailApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    def get_permissions(self):
        self.permission_classes = [AllowAny]
        if self.request.method in ['PUT','PATCH','DELETE']:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()