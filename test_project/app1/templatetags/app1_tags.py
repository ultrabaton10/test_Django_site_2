from django import template
from app1.models import *


register = template.Library()  # instance of Library class example
                               # which let us register all our custom functions.

articles = [
    'Name:',
    'Author:',
    'Category:',
    'Price:'
]


@register.simple_tag(name='categories')
def get_categories():
    return Category.objects.all()

@register.simple_tag(name='products')
def get_products():
    return Products.objects.all()

@register.inclusion_tag('app1/list_categories.html')
def show_all_categories():
    categories = Category.objects.all()
    media_url = '../media/'
    context = {
        'media_url' : media_url,
        'cats': categories,
    }
    return context

@register.inclusion_tag('app1/list_products.html')
def show_chosen_products(cat_selected):
    print(cat_selected, 'cat_selected in def show_chosen_products in app1_tags')
    if int(cat_selected) == 0:
        products = Products.objects.all()
        media_url = '../../media/'
    else:
        # print('-'*10000)
        products = Products.objects.filter(id=cat_selected)
        media_url = '../../../../media/'
    context = {
        'media_url' : media_url,
        'prods': products,
        'articles' : articles,
    }
    return context

@register.inclusion_tag('app1/list_menu_header.html')
def show_menu_bar(header_menu, title):
    context = {
        'header_menu' : header_menu,
        'title' : title,
    }
    print(context['header_menu'][0]['url_name'], 'ojojoj', context['title'], '|||||||||proverka zdes')
    return context



