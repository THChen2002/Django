from django.db import models

# Create your models here.
class student(models.Model):
	stdName = models.CharField(max_length = 50, null = False)
	stdID = models.CharField(max_length = 10, null = False)
	stdSex = models.CharField(max_length = 2, default = "M", null = False)
	stdBirth = models.DateField(null = True)
	stdPhone = models.CharField(max_length = 50, null = True)

	def __str__(self):
		return self.stdName