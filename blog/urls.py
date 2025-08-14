from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.blog, name="blog"),
    path('blog-post/', views.ListCreateBlogApi.as_view(),),
    path('blog-detail/<pk>/', views.BlogDetailApi.as_view(),),

]