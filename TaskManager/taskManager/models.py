from django.db import models

# Create your models here.
class taskManager(models.Model):
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
	Status = models.BooleanField(default=False)

	def __str__(self):
		return self.title
