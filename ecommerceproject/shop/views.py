from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from .models import Category,Products
from django.core.paginator import Paginator,EmptyPage,InvalidPage
def allProdCat(request,c_slug=None):
	c_page=None
	products_list=None
	if c_slug!=None:
		c_page=get_object_or_404(Category,slug=c_slug)
		products_list=Products.objects.all().filter(category=c_page,available=True)
	else:
		products_list=Products.objects.all().filter(available=True)
	paginator=Paginator(products_list,6)
	try:
		page=int(request.GET.get('page','1'))
	except:
		page=1
	try:
		products=paginator.page(page)
	except (EmptyPage,InvalidPage): 
		products=paginator.page(paginator.num_pages)

	return render(request,'category.html',{'category':c_page,'products':products})

def ProDetails(request,c_slug,p_slug):
	try:
		p_page=Products.objects.get(category__slug=c_slug,slug=p_slug)
	except Exception as e:
		raise e
	return render(request,'product.html',{'product':p_page})


	


