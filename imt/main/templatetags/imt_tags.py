from django import template
from django.db.models import Count


from main.models import Category, catDietary

register = template.Library()

@register.inclusion_tag('main/list_category.html')
def get_categories():
    cats = Category.objects.all()
    return {"cats": cats}


@register.inclusion_tag('main/list_category.html')
def get_categories1():
    cats = catDietary.objects.all()
    return {"cats": cats}