from django.contrib.auth.models import User
from rest_framework import serializers
from .models import taskManager

class UserSerializer(serializer.ModelSerializer):
	password = serializers.CharField(write_only=True)

	class Meta:
		model = User
		fields = ['username','email','password']
	
	def create(self, validated_data):
        # Hash the password before saving the user
	        user = User.objects.create_user(
        	    username=validated_data['username'],
            	    email=validated_data['email'],
            	    password=validated_data['password']
        )
        return user

class taskSerializer(serializers.ModelSerializer):
	username = serializers.CharField(source='user.name', read_only=True)
	email = serializers.EmailField(source='user.email', read_only=True)


	class Meta:
		model = taskManager
		fields = '__all__'

	def create(self, validated_data):
		return TaskManager.objects.create(user=self.context['request'].user, **validated_data)
