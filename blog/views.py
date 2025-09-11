from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, AllowAny
from .models import Blog, Comment
from .serializers import BlogSerializer, CommentSerializer

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
    

def blog_detail(request, pk):
    context = {
        "post_id": pk
        }
    return render(request, 'blog_detail.html', context)


class CommentListCreateApi(generics.ListCreateAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        post_id = self.kwargs.get('post_id')
        return Comment.objects.filter(post_id=post_id)

    def perform_create(self, serializer):
        post_id = self.kwargs.get('post_id')
        serializer.save(post_id=post_id)


def event(request):
    context ={

    }
    return render(request, 'event.html',context)