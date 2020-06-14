from django.db import models
from django.contrib.auth.models import User
class ChatUser(models.Model):

	user = models.OneToOneField(User, on_delete = models.CASCADE)

	def __str__(self):
		return self.user.username

class message(models.Model):

	messageText = models.TextField()
	sender = models.CharField(max_length = 50)
	receiver = models.CharField(max_length = 50)
	



# Create your models here.
