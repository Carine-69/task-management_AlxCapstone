from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import TaskViewSet, register, homepage, CustomTokenObtainPairView

router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='tasks') 

urlpatterns = [
    path('', homepage,  name='homepage'),
    path('', include(router.urls)),
    path('auth/register/', register, name='register'),
    path('auth/login/', CustomTokenObtainPairView.as_view(), name='login'),
]
