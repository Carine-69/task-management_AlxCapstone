from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import taskViewSet

router = DefaultRouter()
router.register(r'tasks', taskViewSet) 

urlpatterns = [
    path('api/', include(router.urls)),
]
