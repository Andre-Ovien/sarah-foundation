from rest_framework import serializers
from .models import Blog, Comment



class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            'id',
            'name',
            'email',
            'comment',
            'comment_date',
        )

class BlogSerializer(serializers.ModelSerializer):
    #author = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Blog
        fields = (
            'id',
            'author',
            'title',
            'content',
            'image',
            'publish_date',
            'update_date',
        )