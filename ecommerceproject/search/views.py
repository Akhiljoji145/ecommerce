from django.shortcuts import render
from django.http import HttpResponse
from shop.models import Products
from django.db.models import Q
# Create your views here.
def SearchResult(request):
	products=None
	query=None
	if 'q' in request.GET:
		query=request.GET.get('q')
		if query:
			products=Products.objects.all().filter(Q(name__contains=query) | Q(desc__contains=query)) 
	return render(request,'search.html',{'query':query,'products':products})