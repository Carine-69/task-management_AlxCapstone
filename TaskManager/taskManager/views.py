from django.http import HttpResponse
from django.contrib.auth import get_user_model
from .models import taskManager  
from .serializers import taskSerializer  
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

# Create your views here.

def homepage(request):
	return HttpResponse('Welcome to the Task Manager Home Page!')

class taskViewSet(viewsets.ModelViewSet):  
    serializer_class = taskSerializer  
    permission_classes = [IsAuthenticated]
    queryset = taskManager.objects.all()
 
    def get_queryset(self):
        user = self.request.user
        return taskManager.objects.filter(user=user)  
    
    def perform_create(self, serializers):
        serializers.save(user=self.request.user)  
