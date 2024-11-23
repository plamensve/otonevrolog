from django.db import models
from otonevrolog_main.accounts.models import CustomUser
from otonevrolog_main.accounts.utils import get_current_user


class BlogPost(models.Model):
    TITLE_MAX_LENGTH = 200

    title = models.CharField(
        max_length=TITLE_MAX_LENGTH
    )

    content = models.TextField(

    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    author = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='blog_posts'
    )

    def __str__(self):
        return self.title


class Comment(models.Model):
    AUTHOR_MAX_LENGTH = 100

    author = models.CharField(
        max_length=AUTHOR_MAX_LENGTH
    )

    text = models.TextField(

    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    blog_post = models.ForeignKey(
        BlogPost,
        related_name='comments',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"Comment by {self.author} on {self.blog_post}"
