from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name='shop'
urlpatterns = [
    path('',views.allProdCat,name='main'),
    path('<slug:c_slug>/',views.allProdCat,name='category'),
    path('<slug:c_slug>/<slug:p_slug>/',views.ProDetails,name='prodetails'),
]
