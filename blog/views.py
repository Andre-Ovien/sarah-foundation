from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, AllowAny
from .models import Blog, Comment
from .serializers import BlogSerializer, CommentSerializer
from rest_framework.decorators import api_view


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
    
    @api_view(["GET", "POST"])
    def comments_api(request, post_id):
        if request.method == "GET":
            comments = Comment.objects.filter(post_id=post_id).order_by("-created_at")
            serializer = CommentSerializer(comments, many=True)
            return Response(serializer.data)

        if request.method == "POST":
            data = request.data.copy()
            data["post"] = post_id
            serializer = CommentSerializer(data=data)
            if serializer.is_valid():
                serializer.save(post_id=post_id)
                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)
    

def blog_detail(request, pk):
    recent_post = Blog.objects.order_by('-publish_date')[:3]
    context = {
        "post_id": pk,
        "recent_post": recent_post,
        }
    return render(request, 'blog_detail.html', context)


class CommentListCreateApi(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        post_id = self.kwargs.get('post_id')
        return Comment.objects.filter(blog_id=post_id).order_by("-comment_date")

    def perform_create(self, serializer):
        post_id = self.kwargs.get('post_id')
        blog = Blog.objects.get(pk=post_id)
        serializer.save(blog=blog)