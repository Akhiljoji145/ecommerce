from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Category,Products
def allProdCat(request,c_slug=None):
	c_page=None
	products=None
	if c_slug!=None:
		c_page=get_object_or_404(Category,slug=c_slug)
		products=Products.objects.all().filter(category=c_page,available=True)
	else:
		products=Products.objects.all().filter(available=True)
	return render(request,'category.html',{'category':c_page,'products':products})
