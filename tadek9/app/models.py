from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class post(models.Model):
	body = models.TextField()
	time = models.DateTimeField(auto_now_add = True)


class authpost(models.Model):
	body = models.TextField()
	time = models.DateTimeField(auto_now_add = True)
	owner = models.ForeignKey(User)
