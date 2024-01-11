from django.db import models

# Create your models here.
class Category(models.Model):
	name= models.CharField(max_length=250, unique=True)
	slug=models.SlugField(max_length=250,unique=True)
	desc=models.TextField(blank=True)
	image=models.ImageField(upload_to='cat_img',blank=True)
    def __str__(self):
        return 
class Products(models.Model):
	name=models.CharField(max_length=250)
	slug=models.SlugField(max_length=250,unique=True)
	image=models.ImageField(upload_to='pro_img')
	desc=models.TextField()