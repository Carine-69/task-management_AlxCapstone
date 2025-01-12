from django.db import models
from django.contrib.auth.models import User
# Create your models here.

STATUS_CHOICES = (
	('pending', 'pending'),
	('In progress', 'In progress'),
	('Completed', 'Completed'),
)
class Task(models.Model):
	LOW = 1
	MEDIUM = 2
	HIGH = 3

	PRIORITY_CHOICES = [
		(LOW,'low'),
		(MEDIUM,'medium'),
		(HIGH,'high'),
	]

	title = models.CharField(max_length=200)
	Description = models.TextField()
	Due_Date = models.DateTimeField(auto_now_add=True)
	Priority_Level = models.PositiveIntegerField(
		choices=PRIORITY_CHOICES,
		default=LOW,
	)
	Status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='pending')
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
	def __str__(self):
		return self.title
