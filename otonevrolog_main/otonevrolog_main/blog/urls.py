from django.urls import path
from .views import BlogListView, BlogDetailView, BlogCreateView, EditCommentView, DeleteCommentView

urlpatterns = [
    path('', BlogListView.as_view(), name='blog_list'),
    path('<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('create/', BlogCreateView.as_view(), name='blog_create'),
    path('<int:pk>/edit/', EditCommentView.as_view(), name='edit_comment'),
    path('<int:pk>/delete/', DeleteCommentView.as_view(), name='delete_comment'),
]
