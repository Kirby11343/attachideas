from django.urls import path
from . import views
from .views import ProfileListView, ProfileDetailView, ProfileUpdateView

urlpatterns = [
    path('profile/list/', ProfileListView.as_view(), name='user_profiles'),
    path('profile/<int:pk>/', ProfileDetailView.as_view(), name="profile"),
    path('profile/<int:pk>/edit/', ProfileUpdateView.as_view(), name="profile_edit"),
]