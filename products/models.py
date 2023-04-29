from django.db import models

# Create your models here.

det_choices = [
    ('phones','phones'),
    ('airbods','airbods'),
]


class det(models.Model):
    type = models.CharField(choices=det_choices,max_length=250)
    phones = models.OneToOneField('phones',null=True,blank=True,on_delete=models.PROTECT)
    airbods = models.OneToOneField('airbods',null=True,blank=True,on_delete=models.PROTECT)
    # laptops = models.OneToOneField('laptops',null=True,blank=True,on_delete=models.PROTECT)
    # Womens_perfume = models.OneToOneField('Womens_perfume',null=True,blank=True,on_delete=models.PROTECT)
    # mens_perfume = models.OneToOneField('mens_perfume',null=True,blank=True,on_delete=models.PROTECT)
    

        
    def __str__(self):
        return str(self.id)

class phones(models.Model):
    img = models.ImageField(upload_to='product')
    version = models.CharField(null=True,blank=True,max_length=250)
    internal_memory = models.CharField(null=True,blank=True,max_length=250)
    model_color = models.CharField(null=True,blank=True,max_length=250)
    sim_nm = models.IntegerField(null=True,blank=True)
    g_type = models.IntegerField(null=True,blank=True)


    
    def __str__(self):
        return str(self.id)

class airbods(models.Model):
    img = models.ImageField(upload_to='product')
    version = models.CharField(null=True,blank=True,max_length=250)
    internal_memory = models.CharField(null=True,blank=True,max_length=250)
    model_color = models.CharField(null=True,blank=True,max_length=250)
    sim_nm = models.IntegerField(null=True,blank=True)
    g_type = models.IntegerField(null=True,blank=True)


    
    def __str__(self):
        return str(self.id)