from django.db import models
from django.contrib.auth.models import User
import time
class ChatUser(models.Model):

	user = models.OneToOneField(User, on_delete = models.CASCADE)

	def __str__(self):
		return self.user.username

class Message(models.Model):

	MessageText = models.TextField()
	sender = models.CharField(max_length = 50)
	receiver = models.CharField(max_length = 50)
	time_of_send = models.FloatField()
	



# Create your models here.
