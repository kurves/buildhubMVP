from django.urls import path
from . import views

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, MessageViewSet, UserViewSet



urlpatterns = [
    path('', views.home, name='home'),
    path('project/<int:project_id>/', views.project_detail, name='project_detail'),
    path('post_project/', views.post_project, name='post_project'),
    path('messages/', views.messages, name='messages'),
    path('profile/', views.profile, name='profile'),
]
