from django.contrib import admin
from .models import Products,Category
#Register your models here.
class CategoryAdmin(admin.ModelAdmin):
	list_display=['name','slug']
	prepopulated_fields={'slug':('name',)}
admin.site.register(Category,CategoryAdmin)

class ProductsAdmin(admin.ModelAdmin):
	list_display=['name','slug','stock','price','available','created','updated']
	list_editable=['price','stock','available']
	prepopulated_fields={'slug':('name',)}
admin.site.register(Products,ProductsAdmin)