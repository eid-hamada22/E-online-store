from django.urls import URLPattern,path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('Pcategory', views.Pcategory, name="Pcategory"),
    path('product', views.product, name="product"),
    path('product_test/<str:slug>', views.product_test, name="product_test"),

    
]