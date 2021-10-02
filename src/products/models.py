from django.db import models

# Create your models here.


# we want 
class Product(models.Model):
    title       = models.TextField()
    description = models.TextField()
    price       = models.TextField()