from django.db import models

# Create your models here.
from django.db import models

class students(models.Model):
    Roll_no = models.IntegerField()
    Name = models.CharField(max_length=20)
    Qualification = models.CharField(max_length=20)
    Course_joined = models.CharField(max_length=20)