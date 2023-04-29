from django.shortcuts import render
from . import models
from django.apps import apps
from django import template


# Create your views here.
# ..\Scripts\activate
# python manage.py makemigrations
# python manage.py migrate
# python manage.py runserver
# python manage.py collectstatic 
def index(request):
    return render(request ,'pages/index.html')

def Pcategory(request):
    return render(request ,'pages/Pcategory.html')

def product(request):
    return render(request ,'pages/product.html')

def product_test(request,slug):
    x = 'product'
    prd_model = apps.get_model('pages', x)
    prd = prd_model.objects.get(slug = slug)
    print(prd.category.en_name)
    rel_model = apps.get_model('products', prd.category.en_name)
    rel = rel_model.objects.get(id = prd.rel_id)
    if prd.Pproduct:
        Pproduct = models.Pproduct.objects.get(id = prd.Pproduct.id)
        anther_pre = models.product.objects.filter(Pproduct = Pproduct)
        
        anther_pre_list_id = []
        for item in anther_pre:
            print(item)
            anther_pre_list_id.append(item.rel_id)
            suggested_products = prd.Pproduct.suggested_products.all()
            print(suggested_products)
            suggested_products_id = []
            for item in suggested_products:
                suggested_products_id.append(item.category.id)
            same_suggested_products_category_product = prd_model.objects.filter(category_id__in = suggested_products_id)
            print(same_suggested_products_category_product)
        anther_pre_rel = rel_model.objects.filter(id__in = anther_pre_list_id)

    else:  
        same_suggested_products_category_product = 0
        anther_pre_rel = 0
        anther_pre = 0
    print(anther_pre_rel)
    same_Brand_product = prd_model.objects.filter(Brand = prd.Brand)
    same_category_product = prd_model.objects.filter(category = prd.category)
    same_cart_product = 0
    

    x = {
        'prd':prd,
        'anther_pre':anther_pre,
        'rel':rel,
        'anther_pre_rel':anther_pre_rel,
        'same_Brand_product':same_Brand_product,
        'same_category_product':same_category_product,
        'same_suggested_products_category_product':same_suggested_products_category_product,
        'same_cart_product':same_cart_product,
    }
    return render(request ,'pages/product_test.html',x)