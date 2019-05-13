from django.urls import path

from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView

from django.contrib.auth import login

urlpatterns = [
    path('', PostListView.as_view(), name='mainPage'),
    path('user/<str:username>/', UserPostListView.as_view(), name='user_posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/master/', PostCreateView.as_view(), name='post_master'),
    path('post/<int:pk>/master', PostUpdateView.as_view(), name='post_update_master'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post_delete'),
]