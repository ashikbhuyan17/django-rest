from django.db import models

# Create your models here.
from unicodedata import name
from django.db import models

# Create your models here.
class Students(models.Model):
    name = models.CharField(max_length=50)
    roll = models.IntegerField()
    city = models.CharField(max_length=50)
    phone = models.IntegerField()

    
    def __str__(self):
        return self.name


