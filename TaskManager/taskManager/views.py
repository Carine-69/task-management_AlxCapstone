from django.contrib.auth import get_user_model
from .models import taskManager
from .Serializer import taskSerializer
from rest_framework import Viewsets
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class taskViewSet(ViewSets.ModelViewSet):
	serializer_class = taskSerializer
	permission_classes = [IsAuthenticated]

#this is to use ViewSet to handle CRUD operations
	def get_self_quaryset(self):
		user = self.request.user
		return taskMnager.objects.filter(user=user)

#this is to make sure that the user only sees and manage his/her own tasks only

	def save_creation(self):
		serializer.save(user=self.request.user)

#this is to automatically save user field 




