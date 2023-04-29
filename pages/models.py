
from distutils.command.upload import upload
import imghdr
from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
import random
from products import models as products_models
from django.core.validators import MinValueValidator, MaxValueValidator
class user(models.Model):
    fname = models.CharField(max_length=10)
    lname = models.CharField(max_length=10)
    password = models.CharField(max_length=50)
    email = models.EmailField(max_length=20)
    gender = models.CharField(max_length=20,choices=(('male','male'),('female','female')))
    age = models.IntegerField(default=0,)
    phone = models.IntegerField()
    published_at = models.DateTimeField(auto_now=True)
    h_purchase = models.BooleanField(default=False)
    def __str__(self):
        return self.email




    
    
# class Order(models.Model):
#     # customer = models.ForeignKey(Customer, on_delete=models.PROTECT, null=True, blank=True)
#     date_ordered = models.DateTimeField(auto_now_add=True)
#     complete = models.BooleanField(default=False)
#     transaction_id = models.CharField(max_length=100, null=True)
#     @property
#     def get_cart_total(self):
#         orderitems = self.orderitem_set.all()
#         total = sum([item.get_total for item in orderitems])
#         return total
    
# class OrderItem(models.Model):
#     product = models.ForeignKey(product, on_delete=models.PROTECT, null=True)
#     order = models.ForeignKey(Order, on_delete=models.PROTECT, null=True)
#     quantity = models.IntegerField(default=0, null=True, blank=True)
#     date_added = models.DateTimeField(auto_now_add=True)
    
#     @property
#     def get_total(self):
#         total = self.product.price * self.quantity
#         return total


class Brand(models.Model):
    name = models.CharField(max_length=250)
    category = models.ManyToManyField('category')
    published_at = models.DateTimeField(auto_now=True)
    img = models.ImageField()
    
    def save(self,*args, **kwargs):
        self.slug = slugify(self.name)
        super(Brand,self).save(*args, **kwargs)
    def __str__(self):
        return self.name
    
class Pcategory(models.Model):
    en_name = models.CharField(max_length=250)
    ar_name = models.CharField(max_length=250)
    published_at = models.DateTimeField(auto_now=True)
    img = models.ImageField()
    similar_Pcategory = models.ForeignKey('self',null=True,blank=True,on_delete=models.PROTECT)


    def __str__(self):
        return str(self.en_name)
    
class category(models.Model):
    en_name = models.CharField(max_length=250)
    ar_name = models.CharField(max_length=250)
    pcategory = models.ForeignKey(Pcategory,null=True,blank=True,on_delete=models.PROTECT)
    published_at = models.DateTimeField(auto_now=True)
    similar_category = models.ManyToManyField('self',blank=True)
    img = models.ImageField()
    priority = models.IntegerField(choices=[(1,1),(2,2),(3,3),])
    
    def save(self,*args, **kwargs):
        self.slug = slugify(self.en_name)
        super(category,self).save(*args, **kwargs)
    def __str__(self):
        return str(self.en_name)

def product_image_upload(instance,filename):
    imagename , extension = filename.split(".")
    return f"product/{instance.category}/{instance.slug}.{extension}"

class Pproduct(models.Model):
    name = models.CharField(max_length=250)
    Product_number = models.IntegerField(unique=True,blank=True, null=True)
    published_at = models.DateTimeField(auto_now=True)
    Brand = models.ForeignKey('Brand',null=True,on_delete=models.PROTECT)
    category = models.ForeignKey('category',null=True,on_delete=models.PROTECT)
    suggested_products =  models.ManyToManyField('product')
    def save(self,*args, **kwargs):
        self.Product_number = random.randrange(100000, 1000000)
        super(Pproduct,self).save(*args, **kwargs)
        
    def __str__(self):
        return self.name
    
class product(models.Model):
    Pproduct = models.ForeignKey(Pproduct,null=True,blank=True,on_delete=models.PROTECT)
    name = models.CharField(max_length=250)
    ar_name = models.CharField(max_length=250)
    Product_number = models.IntegerField(unique=True,blank=True, null=True)
    published_at = models.DateTimeField(auto_now=True)
    Brand = models.ForeignKey('Brand',null=True,on_delete=models.PROTECT)
    bio = models.TextField(verbose_name='bio    <li></li>   ',max_length=100)
    price = models.IntegerField()
    lprice = models.IntegerField(null=True,blank=True)
    Discount = models.IntegerField(null=True,blank=True)
    category = models.ForeignKey('category',null=True,on_delete=models.PROTECT)
    slug = models.SlugField(unique=True,blank=True, null=True)
    img = models.ImageField(upload_to='product')
    secondary_image = models.ManyToManyField('secondary_image',max_length=3,blank=True)
    det = models.OneToOneField(products_models.det,null=True,blank=True,on_delete=models.PROTECT)
    rel_id = models.IntegerField()
    
    def save(self,*args, **kwargs):
        self.slug = slugify(self.name,self.id)
        self.Product_number = random.randrange(100000, 1000000)
        super(product,self).save(*args, **kwargs)
        
    def __str__(self):
        return self.slug
    

class secondary_image(models.Model):
    rate = models.IntegerField(choices=[(1,1),(2,2),(3,3),])
    img = models.ImageField(upload_to='product')


    def __str__(self):
        return str(self.id)







