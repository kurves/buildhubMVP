from django.urls import path
from . import views
from .views import home, post_project, update_profile

urlpatterns = [
    path('', home, name='home'),
    path('post_project/', post_project, name='post_project'),
    path('update_profile/', update_profile, name='update_profile'),
]


urlpatterns = [
    path('', views.home, name='home'),
    path('project/<int:project_id>/', views.project_detail, name='project_detail'),
    path('post_project/', views.post_project, name='post_project'),
    path('messages/', views.messages, name='messages'),
    path('profile/', views.profile, name='profile'),
]
