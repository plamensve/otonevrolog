from django.db import models
from otonevrolog_main.accounts.models import CustomUser
from otonevrolog_main.accounts.utils import get_current_user
from otonevrolog_main.blog.validators import validate_image_size


class BlogPost(models.Model):
    TITLE_MAX_LENGTH = 200
    CONTENT_MAX_LENGTH = 300

    title = models.CharField(
        max_length=TITLE_MAX_LENGTH
    )

    content = models.TextField(
        max_length=CONTENT_MAX_LENGTH,
        null=True,
        blank=True,
        help_text='Optional'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    blog_post_image = models.ImageField(
        blank=True,
        null=True,
        validators=[
            validate_image_size
        ]
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
    TEXT_MAX_LENGTH = 300

    author = models.CharField(
        max_length=AUTHOR_MAX_LENGTH
    )

    text = models.TextField(
        max_length=TEXT_MAX_LENGTH,
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
