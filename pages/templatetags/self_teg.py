from django import template
from django.apps import apps

register = template.Library()
@register.simple_tag
def get_href_from_rel(model_name,rel_id):
    rel_model = apps.get_model('products', model_name)
    rel = rel_model.objects.get(id = rel_id)

    prd_model = apps.get_model('pages', 'product')
    prd = prd_model.objects.get(rel_id = rel_id)

    return prd.slug

