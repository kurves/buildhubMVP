

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, MessageViewSet, UserViewSet

router = DefaultRouter()
router.register(r'projects', ProjectViewSet)
router.register(r'messages', MessageViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]

""""
urlpatterns = [
    path('', views.home, name='home'),
    path('project/<int:project_id>/', views.project_detail, name='project_detail'),
    path('post_project/', views.post_project, name='post_project'),
    path('messages/', views.messages, name='messages'),
    path('profile/', views.profile, name='profile'),
]
"""