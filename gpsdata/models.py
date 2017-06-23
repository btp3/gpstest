from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Location(models.Model):

	user=models.ForeignKey(User)
	latitude=models.CharField(max_length=250)
	longitude=models.CharField(max_length=250,null=True,blank=False)

	def __str__(self):
		return self.user.username+":("+self.latitude+","+self.longitude+")"