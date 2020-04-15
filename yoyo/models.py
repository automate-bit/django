from django.db import models

class name(models.Model):
	course=models.CharField(max_length=200)
	co=models.CharField(max_length=200)
	def __str__(self):
		return  self.course

class bio(models.Model):
	bo=models.ForeignKey(name,on_delete=models.CASCADE)
	SP=models.CharField(max_length=200)
	j=models.CharField(max_length=200)
