from django.urls import path
from . import views

app_name='cart'
urlpatterns = [
	path('add/<int:product_id>/',views.add_cart,name='add_cart'),
    path('',views.cart_details,name='cart_details'),
    path('delete/<int:product_id>/',views.cart_delete,name='cart_delete'),
    path('remove/<int:product_id>/',views.full_remove,name='remove'),
]
