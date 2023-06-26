from django.shortcuts import render, HttpResponse
from django.urls import reverse_lazy
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
        title = 'Create'
        context['header_menu'] = header_menu
        context['title'] = title
        return context





# def products(request):
#     print(request)
#     if 'GET' == request.method:
#         title = Products
#         context = {
#             'title' : title,
#         }
#         return render(request, 'app1/products.html', context)

    # if request.POST:
    #     # return HttpResponse('<h1><b>Hello World!</b></h1>')
    #     types = Products(
    #         name=request.POST['name'],
    #         author=request.POST['author'],
    #         category=request.POST['category'],
    #         price=request.POST['price']
    #     )
    #     types.save()
    # return HttpResponse('<br>'.join(prod.name for prod in Products.objects.all()))



def categories(request):
    title = 'Categories'
    context = {
        'title' : title,
        'header_menu': header_menu,
    }
    return render(request, 'app1/categories.html', context)




header_menu = [
    {'url_name' : 'index', 'title' : 'Book Shop'},
    {'url_name' : r'products_by_category', 'title' : 'Products'},
    {'url_name' : 'categories', 'title' : 'Categories'},
    {'url_name' : 'create', 'title' : 'Create'},
]

def index(request):
    title = 'Book Shop'
    context = {
        'title' : title,
        'header_menu' : header_menu,
    }
    return render(request, 'app1/index.html', context)



def products_by_category(request, cat_id : int):
    print(cat_id)
    cat_id = cat_id
    title = 'Products'
    context = {
        'title' : title,
        'header_menu': header_menu,
        'cat_id' : cat_id,
    }
    return render(request, 'app1/products.html', context)










def csrf_failure(request, reason=""):
    return HttpResponse('Ti papal suda potomu chto ti dayn idi pomoisya durachok')