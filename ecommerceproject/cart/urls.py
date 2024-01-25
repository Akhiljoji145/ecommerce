from django.urls import path
from . import views

app_name='cart'
urlpatterns = [
    path('',views._cart_id,name='cart'),
]
