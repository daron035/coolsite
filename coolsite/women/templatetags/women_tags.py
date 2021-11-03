from django import template
from women.models import *

register = template.Library()

@register.simple_tag(name='getcats') # простой тег, возвращающая коллекцию из бд
def get_categories():
    return Category.objects.all()

@register.inclusion_tag('women/list_categories.html') # включающий тег
def show_categories():
    cats = Category.objects.all()
    return {"cats": cats}    