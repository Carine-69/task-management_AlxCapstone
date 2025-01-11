from rest_framework.esponse import Response
from res_framework.decorators import api_view
from django.contrib.auth import get_user_model
from .models import taskManager  
from .serializers import UserSerializer, taskSerializer  
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated

# Create your views here.

@api_view(['POST'])
def register(request):
	if request.method == 'POST':
		serializer = UserSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class taskViewSet(viewsets.ModelViewSet):  
    serializer_class = taskSerializer  
    permission_classes = [IsAuthenticated]
    queryset = taskManager.objects.all()
 
    def get_queryset(self):
        user = self.request.user
        return taskManager.objects.filter(user=user)  
    
    def perform_create(self, serializers):
        serializers.save(user=self.request.user)  
