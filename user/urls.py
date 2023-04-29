from django.urls import URLPattern,path
from . import views

app_name = 'user'

urlpatterns = [
    path('', views.user, name="user"),
    path('balance', views.balance, name="balance"),
    path('customers_service', views.customers_service, name="customers_service"),
    path('delivery_address', views.delivery_address, name="delivery_address"),
    path('information', views.information, name="information"),
    path('preferences', views.preferences, name="preferences"),
    path('previous_baskets', views.previous_baskets, name="previous_baskets"),
    path('previous_orders', views.previous_orders, name="previous_orders"),
    path('view_products', views.view_products, name="view_products"),
    
]