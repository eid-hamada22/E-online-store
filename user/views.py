from django.shortcuts import render

# Create your views here.

# python manage.py runserver 1000
# python manage.py startapp appname
def user(request):
    return render(request ,'user/user.html')

def balance(request):
    return render(request ,'user/balance.html')

def customers_service(request):
    return render(request ,'user/customers_service.html')

def delivery_address(request):
    return render(request ,'user/delivery_address.html')

def information(request):
    return render(request ,'user/information.html')

def preferences(request):
    return render(request ,'user/preferences.html')

def previous_baskets(request):
    return render(request ,'user/previous_baskets.html')

def previous_orders(request):
    return render(request ,'user/previous_orders.html')

def view_products(request):
    return render(request ,'user/view_products.html')

