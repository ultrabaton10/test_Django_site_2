from django.shortcuts import render, reverse, redirect, HttpResponse
from django.template import loader
from django.urls import reverse_lazy

from .models import Products, Category

from django.views.generic.edit import CreateView
from .forms import ProductForm


class ProductCreateView(CreateView):
    '''
    Этот класс-контроллер наследуется от базового класса CreateView
    из модуля django.views.generic.edit. Базовый класс реализует функционал
    создания формы, выведением её на экран пользователя с применением
    указанного шаблона хранящегося в переменной template_name,
    получению данных из формы, проверку данных на корректность.
    Потом эти данные заносятся в новую запись в базе данных.
    Если всё прошло успешно, то пользователя перенаправят на другую страницу.

    Переменные:
        template_name --> путь к файлу шаблона - html,
        что будет отображать страницу с формой
        form_class --> класс формы связанный с моделью
        success_url --> адрес html - страницы, на которую
        будет перенаправлен пользователь после успешного занесения
        отправленных в форму данных в базу данных модели Products
    Документация Владимира Дронова к классу CreateView и описание работы
    с формами на странице 63 или 62
    '''
    template_name = 'app1/create_new_product.html'
    form_class = ProductForm
    # model = Products
    success_url = reverse_lazy('create')

    def get_context_data(self, **kwargs):
        '''
        Метод для нашего класса ProductCreateView --> get_context_data
        переопределён для того, чтобы добавить в контекст шаблона
        дополнительные данные: список продуктов и категорий
        в навигации формы. То есть в нашей форме будет раздел навигации,
        в которой будут перечислены разные продукты.
        Для этого мы определили для переменной context
        новое пространство значений дописав ['categories'] и ['products']
        после context и закинули туда все категории и продукты из базы данных.
        :param context : get_context_data(**kwargs)
        :return context
        '''
        context = super().get_context_data(**kwargs)
        return context


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
        't' : t,
        'logic_photo' : '''{% if product.image != '' and not t %}
        ../media/{{ product.image }}
        {% endif %}

        {% if product.image == '' and not t %}
        ../media/my_face.png
        {% endif %}

        {% if t %}
          ../../../../media/{{ product.image }}
        {% endif %}

        {% if product.image == '' and t %}
          ../../../../media/my_face.png
        {% endif %}''',
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

def csrf_failure(request, reason=""):
    return HttpResponse('Ti papal suda potomu chto ti dayn idi pomoisya durachok')