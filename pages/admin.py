from django.contrib import admin
from . import models

# admin.site.register(models.user)
# admin.site.register(models.product)
# admin.site.register(models.Pproduct)
# admin.site.register(models.Pcategory)
# admin.site.register(models.Category)
# admin.site.register(models.Brand)
# admin.site.register(models.types)

from django.apps import apps
from django.contrib.admin.sites import AlreadyRegistered

from django.contrib.auth.models import Group,User

admin.site.unregister(Group)
admin.site.unregister(User)




app_models = apps.get_app_config('pages').get_models()
for model in app_models:
    try:
        admin.site.register(model)
    except AlreadyRegistered:
        pass
    
app_models = apps.get_app_config('products').get_models()
for model in app_models:
    try:
        admin.site.register(model)
    except AlreadyRegistered:
        pass
class SystemAdmin(admin.ModelAdmin):
    filter_horizontal = ('suggested_products',) 

admin.site.unregister(models.Pproduct)
admin.site.register(models.Pproduct,SystemAdmin)
