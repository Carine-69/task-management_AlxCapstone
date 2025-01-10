from rest_framework import serializers
from .models import taskManager

class taskSerializer(serializers.ModelSerializer):
	username = serializer.CharField(source='user.name', read_only=True)
	email = serializer.EmailField(source='user.email', read_only=True)
	password = serializer.CharField(write_only=True)
# define aditional fields
	class Meta:
		model = taskManager
		fields='__all__'
		extra_fields = ['username','email','password']
# this convert the serializer.py into JSON format

	def create(self, validated_data):
		passwod = validated_data.pop('password', None)
		if password:
			taskManager.user.set_password(password)
			taskManager.user.save()
		return taskManager

# this is to handle password during creation
