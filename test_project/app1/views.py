from django.shortcuts import render, reverse, redirect, HttpResponse
from django.template import loader
from .models import Products, Category


def products(request):
    print(request)
    if 'GET' == request.method:
        products = Products.objects.all()
        media_url = 'media/app1/'
        context = {
            'products' : products,
            'media_url' : media_url,
        }
        return render(request, 'app1/products.html', context)

    if request.POST:
        # return HttpResponse('<h1><b>Hello World!</b></h1>')
        types = Products(
            name=request.POST['name'],
            author=request.POST['author'],
            category=request.POST['category'],
            price=request.POST['price']
        )
        types.save()
    return HttpResponse('<br>'.join(prod.name for prod in Products.objects.all()))


def index(request):
    return render(request, 'app1/index.html')

def categories(request):
    cats = Category.objects.all()
    t = False
    context = {
        'cats' : cats,
        't' : t
    }
    return render(request, 'app1/categories.html', context)

def products_by_category(request, cat_id):  #
    products_by_cat = Products.objects.filter(category_id=cat_id)
    t = True
    context = {
        'products' : products_by_cat,
        't' : t,
    }
    return render(request, 'app1/products.html', context)