
from django.db import models


class Books(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField(default=0,null=True)
    in_stock = models.BooleanField(default=True)




    class Meta:
        verbose_name_plural = 'Books'


    def __str__(self):
        return self.title