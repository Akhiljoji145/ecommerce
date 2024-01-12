from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    desc = models.TextField(blank=True)
    image = models.ImageField(upload_to='cat_img', blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return '{}'.format(self.name)




class Products(models.Model):
	name=models.CharField(max_length=250)
	slug=models.SlugField(max_length=250,unique=True)
	image=models.ImageField(upload_to='pro_img')
	desc=models.TextField()
	category=models.ForeignKey(Category,on_delete=models.CASCADE)
	stock=models.IntegerField()
	price=models.DecimalField(max_digits=10,decimal_places=2)
	available=models.BooleanField(default=True)
	created=models.DateTimeField(auto_now_add=True)
	updated=models.DateTimeField(auto_now=True)
	class Meta:
		ordering=('name',)
		verbose_name='product'
		verbose_name_plural='products'
	def __str__(self):
		return '{}'.format(self.name)