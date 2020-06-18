from django.db import models

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=1000)
    age=models.IntegerField()
    status=models.BooleanField()