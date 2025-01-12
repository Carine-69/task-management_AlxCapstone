from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import Task
from .serializers import TaskSerializer, UserSerializer


# Home Page View
def homepage(request):
    return HttpResponse('Welcome to the Task Manager Home Page!')


# Custom JWT Login View
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Add custom claims to the token
        token['username'] = user.username
        return token


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


# User Registration View
@api_view(['POST'])
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(
            {"message": "User registered successfully!"},
            status=status.HTTP_201_CREATED
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Task ViewSet
class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    queryset = Task.objects.all()

    def get_queryset(self):
        """Return tasks belonging to the authenticated user only."""
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        """Assign the task to the authenticated user."""
        serializer.save(user=self.request.user)
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import Task
from .serializers import TaskSerializer, UserSerializer


# Home Page View
def homepage(request):
    return HttpResponse('Welcome to the Task Manager Home Page!')


# Custom JWT Login View
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Add custom claims to the token
        token['username'] = user.username
        return token


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


# User Registration View
@api_view(['POST'])
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(
            {"message": "User registered successfully!"},
            status=status.HTTP_201_CREATED
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Task ViewSet
class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Return tasks belonging to the authenticated user only."""
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        """Assign the task to the authenticated user."""
        serializer.save(user=self.request.user)

    def update(self, request, *args, **kwargs):
        """Prevent updating completed tasks unless reverted to incomplete."""
        partial = kwargs.pop('partial', False)
        instance = self.get_object()

        if instance.status == 'Completed' and request.data.get('status') != 'Pending':
            return Response(
                {"error": "Completed tasks cannot be edited unless reverted to Pending."},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        """Ensure the task belongs to the authenticated user before deleting."""
        instance = self.get_object()
        if instance.user != request.user:
            return Response(
                {"error": "You are not authorized to delete this task."},
                status=status.HTTP_403_FORBIDDEN
            )
        self.perform_destroy(instance)
        return Response(
            {"message": "Task deleted successfully!"},
            status=status.HTTP_204_NO_CONTENT
        )

    def update(self, request, *args, **kwargs):
        """Prevent updating completed tasks unless reverted to incomplete."""
        partial = kwargs.pop('partial', False)
        instance = self.get_object()

        if instance.status == 'Completed' and request.data.get('status') != 'Pending':
            return Response(
                {"error": "Completed tasks cannot be edited unless reverted to Pending."},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        """Ensure the task belongs to the authenticated user before deleting."""
        instance = self.get_object()
        if instance.user != request.user:
            return Response(
                {"error": "You are not authorized to delete this task."},
                status=status.HTTP_403_FORBIDDEN
            )
        self.perform_destroy(instance)
        return Response(
            {"message": "Task deleted successfully!"},
            status=status.HTTP_204_NO_CONTENT
        )
