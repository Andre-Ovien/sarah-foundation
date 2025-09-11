from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.blog, name="blog"),
    path('events/', views.event, name="event"),
    path('posts-detail/<int:pk>/', views.blog_detail, name="post_detail"),
    path('blog-post/', views.ListCreateBlogApi.as_view(),),
    path('blog-detail/<pk>/', views.BlogDetailApi.as_view(),),
    path('blog/<int:post_id>/comments/', views.CommentListCreateApi.as_view(), name='post-comments'),

]