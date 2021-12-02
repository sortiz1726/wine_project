from django.db import models

# Create your models here.
class Wine(models.Model):
    wine_name = models.CharField(max_length = 256)
    price = models.CharField(max_length = 10)
    varietal = models.CharField(max_length = 255)
    description = models.TextField()

    def __str__(self):
        return self.wine_name