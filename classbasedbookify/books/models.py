from django.db import models

# Create your models here.
class Books(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField(default=0, null=True)
    in_stock = models.BooleanField(default=True)

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Book'
        verbose_name_plural = 'Books'

    def __str__(self):
        return self.title
            