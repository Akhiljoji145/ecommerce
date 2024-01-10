from django.db import models

# Create your models here.
class Products(models.Model):
	name= models.CharField(max_length=250, unique=True)
	slug=models.SlugField(max_length=250,unique=True)

    def __str__(self):
        return 
