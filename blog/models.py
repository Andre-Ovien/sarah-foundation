from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify



class User(AbstractUser):
    pass

class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="post_author")
    title = models.CharField(max_length=264, verbose_name="Add a title")
    slug = models.SlugField(max_length=264, unique=True)
    content = models.TextField(verbose_name="What's on your mind?")
    image = models.ImageField(upload_to="blog_image", verbose_name="Add an image")
    publish_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-publish_date']

    def __str__(self):
        return self.title


class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="blog_comment")
    name = models.CharField(max_length=50)
    email = models.EmailField()
    comment = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-comment_date']

    def __str__(self):
        return self.comment


class Likes(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="liked_blog")