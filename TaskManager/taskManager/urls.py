from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import taskViewSet

router = DefaultRouter()
router.register(r'tasks', views.taskViewSet) 

urlpatterns = [
    path('tasks/', include(router.urls)),
    path('',views.homepage, name='homepage'),
]
