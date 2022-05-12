
from django.db import models


class TimeStamppedModel(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
 

class SellingPlatform(TimeStamppedModel):
    name = models.CharField(max_length=100)
    about = models.TextField()
    website_url = models.URLField(max_length=150)
 
    def __str__(self):
        return self.name


class BookList(TimeStamppedModel):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField(default=0,null=True)
    in_stock = models.BooleanField(default=True)
    selling_platform = models.ForeignKey(SellingPlatform,on_delete=models.CASCADE,related_name='booklists')

    class Meta:
        verbose_name_plural = 'Book Lists'


    def __str__(self):
        return self.title