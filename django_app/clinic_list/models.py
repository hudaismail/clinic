from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Products(models.Model):
    name = models.CharField(max_length=100)
    img  = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price= models.IntegerField()
    offer= models.BooleanField(default=False)


