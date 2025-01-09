from django.url import path include
from rest_framework import DefaultRouter
from .views import taskViewSet

router = DefaultRouter
router.register(r'tasks', taskViewSet)
urlpatterns = ['api/'include(router.urls),]
