from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name='shop'
urlpatterns = [
    path('',views.allProdCat,name='main'),
    path('<slug:c_slug>/',views.allProdCat,name='category'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)