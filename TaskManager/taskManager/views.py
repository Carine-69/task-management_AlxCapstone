from django.contrib.auth import get_user_model
from .models import taskManager  
from .Serializer import taskSerializer  
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class taskViewSet(viewsets.ModelViewSet):  
    serializer_class = taskSerializer  
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return taskManager.objects.filter(user=user)  
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)  
