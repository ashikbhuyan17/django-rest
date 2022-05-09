from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    age=models.IntegerField()
    email=models.EmailField(max_length=100)
    phone=models.IntegerField()
    address=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    roll = models.IntegerField()