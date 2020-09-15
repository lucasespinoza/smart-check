from django.db import models

# Create your models here.

class User(models.Model):
	userId = models.AutoField(primary_key = True)
	userName = models.CharField(max_length = 100)
	userLastName = models.CharField(max_length = 100)
	userEmail = models.EmailField(max_length = 255)

	def __str__(self):
		return self.userName