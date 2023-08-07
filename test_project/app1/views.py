from django.shortcuts import render, HttpResponse
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import *



header_menu = [
    {'url_name' : r'index', 'title' : 'Book Shop'},
]

std_media_url = '../media/'

def set_blank_image_if_book_image_not_exist():
    for book in Book.objects.all():
        if book.book_img == "":
            book.book_img = "blank-image.png"

# class BookCreateView(CreateView):
#     '''
#     Этот класс-контроллер наследуется от базового класса CreateView
#     из модуля django.views.generic.edit. Базовый класс реализует функционал
#     создания формы, выведением её на экран пользователя с применением
#     указанного шаблона хранящегося в переменной template_name,
#     получению данных из формы, проверку данных на корректность.
#     Потом эти данные заносятся в новую запись в базе данных.
#     Если всё прошло успешно, то пользователя перенаправят на другую страницу.
#
#     Переменные:
#         template_name --> путь к файлу шаблона - html,
#         что будет отображать страницу с формой
#         form_class --> класс формы связанный с моделью
#         success_url --> адрес html - страницы, на которую
#         будет перенаправлен пользователь после успешного занесения
#         отправленных в форму данных в базу данных модели Products
#     Документация Владимира Дронова к классу CreateView и описание работы
#     с формами на странице 63 или 62
#     '''
#     template_name = 'app1/create_new_product.html'
#     form_class = BookForm
#     success_url = reverse_lazy('create')
#
#     def get_context_data(self, **kwargs):
#         print('get_context_data_func, Hello!!!')
#         '''
#         Метод для нашего класса BookCreateView --> get_context_data
#         переопределён для того, чтобы добавить в контекст шаблона
#         дополнительные данные: список продуктов и категорий
#         в навигации формы. То есть в нашей форме будет раздел навигации,
#         в которой будут перечислены разные продукты.
#         Для этого мы определили для переменной context
#         новое пространство значений дописав ['categories'] и ['products']
#         после context и закинули туда все категории и продукты из базы данных.
#         :param context : get_context_data(**kwargs)
#         :return context
#         '''
#
#         context = super().get_context_data(**kwargs)
#         title = 'Create'
#         context['header_menu'] = header_menu
#         context['title'] = title
#         return context

# def products(request):
#     print(request)
#     if 'GET' == request.method:
#         title = Products
#         context = {
#             'title' : title,
#         }
#         return render(request, 'UPLOADED_USERS_IMAGESS/products.html', context)

    # if request.POST:
    #     # return HttpResponse('<h1><b>Hello World!</b></h1>')
    #     types = Products(
    #         book_name=request.POST['book_name'],
    #         book_author=request.POST['book_author'],
    #         book_category=request.POST['book_category'],
    #         current_price=request.POST['current_price']
    #     )
    #     types.save()
    # return HttpResponse('<br>'.join(prod.book_name for prod in Products.objects.all()))


# def index(request):
#     print("=-"*10, request.GET, ' --> index page request', "-="*10)
#     title = 'Book Shop'
#     context = {
#         'title' : title,
#         'header_menu' : header_menu,
#         'make_books_text_active' : True,
#     }
#     return render(request, 'app1/index.html', context)


# def categories(request):
#     print("=-" * 10, request.GET, ' categories -->  page request', "-=" * 10)
#     title = 'Categories'
#     context = {
#         'title' : title,
#         'header_menu': header_menu,
#     }
#     return render(request, 'app1/categories.html', context)


def chosen_book(request, book_slug, book_id):
    '''
    Функция, ведущая на страницу product.html,
    на которой отображается карточка с продуктом,
    '''
    print("=-" * 10, request.GET, ' chosen_book -->  page request', "-=" * 10)
    title = 'Self Book Card'
    book_info = db_converter(books_query_set=[[Book.objects.get(pk=book_id)]], all=False)
    context = {
        'title': title,
        'header_menu': header_menu,
        'book_info': book_info,
        'allowance_show_filter_zone': False,
        'make_books_text_active': True,
    }
    return render(request, 'app1/product.html', context)


def return_book_objects_all():
    books_query_set = []
    books_query_set.append(Book.objects.all())
    new_books_query_set = db_converter(books_query_set, True)
    print('def return_book_objects_all():\n\tres --> ', new_books_query_set)
    return new_books_query_set

def index(request):
    '''
    Страница с отфильтрованными книгами.
    Книги фильтруются двумя путями:
    Первый - это когда пользователь перешел на страницу,
    предварительно не применив фильтры, в этом случае будут выведены все продукты.
    Второй - это когда пользователь предварительно
    применил фильтры по категориям продуктов, и в результате ему
    показывается отфильтрованная страница с выбранными продуктами.
    '''
    global new_books_query_set
    title = 'Books'
    # set_blank_image_if_book_image_not_exist()
    print("~-" * 10, request.GET, 'request --> index page', "-~" * 10)
    books_query_set = []
    make_books_text_active = True
    if request.GET.get('detective') is not None or request.GET.get('fantasy') is not None or request.GET.get('business-literature') is not None or request.GET.get('for-little-ones') is not None or request.GET.get('thriller') is not None:
        books_query_set.clear()
        if request.GET.get('detective') is not None:
            print('request.GET.get("detective") -->', request.GET.get("detective"))
            books_query_set.append(Book.objects.filter(book_category=request.GET.get("detective")))
        if request.GET.get('fantasy') is not None:
            books_query_set.append(Book.objects.filter(book_category=request.GET.get("fantasy")))
            print('request.GET.get("fantasy") -->', request.GET.get("fantasy"))
        if request.GET.get('business-literature') is not None:
            books_query_set.append(Book.objects.filter(book_category=request.GET.get("business-literature")))
            print('request.GET.get("business-literature") -->', request.GET.get("business-literature"))
        if request.GET.get('for-little-ones') is not None:
            books_query_set.append(Book.objects.filter(book_category=request.GET.get("for-little-ones")))
            print('request.GET.get("for-little-ones") -->', request.GET.get("for-little-ones"))
        if request.GET.get('thriller') is not None:
            books_query_set.append(Book.objects.filter(book_category=request.GET.get("thriller")))
            print('request.GET.get("thriller") -->', request.GET.get("thriller"))
        new_books_query_set = db_converter(books_query_set, False)
    elif 'req_key' in request.GET:
        req_value = request.GET.get('req_key')
        print('Hello'*100)
        if req_value:
            print('OGOGGOGO'*5)
            try:
                response = Book.objects.get(book_name=req_value)
                print("Good trying")
                title = 'Self Book Card'
                book_info = db_converter(books_query_set=[[Book.objects.get(pk=response.pk)]], all=False)
                context = {
                    'title': title,
                    'header_menu': header_menu,
                    'book_info': book_info,
                    'allowance_show_filter_zone': False,
                    'make_books_text_active': True,
                }
                return render(request, 'app1/product.html', context)
            except Exception:
                print('Bad trying')
                new_books_query_set = return_book_objects_all()
                make_books_text_active = False
                context = {
                    'title': title,
                    'header_menu': header_menu,
                    'books_lst': new_books_query_set,
                    'media_url': std_media_url,
                    'make_books_text_active': make_books_text_active,
                    'allowance_show_filter_zone': True,
                }
                return render(request, 'app1/books_page.html', context)
    else:
        new_books_query_set = return_book_objects_all()
        make_books_text_active = False

    context = {
        'title': title,
        'header_menu': header_menu,
        'books_lst': new_books_query_set,
        'media_url': std_media_url,
        'make_books_text_active': make_books_text_active,
        'allowance_show_filter_zone': True,
    }

    return render(request, 'app1/index.html', context)


def calc_percent(current_price, previous_price):
    c = current_price
    p = previous_price
    percent = ((p - c) / p) * 100
    return percent


def db_converter(books_query_set, all : bool) -> list[dict]:
    global proper_query_set, new_books_query_set
    if all:
        proper_query_set = books_query_set[0]
        new_books_query_set = [{} for _ in range(len(proper_query_set))]
        count = 0
        for book in proper_query_set:
            print('book ----', book)
            new_books_query_set[count]['book_id'] = book.pk
            new_books_query_set[count]['book_name'] = book.book_name
            new_books_query_set[count]['book_slug'] = book.book_slug
            new_books_query_set[count]['book_img'] = book.book_img
            new_books_query_set[count]['book_category'] = book.book_category
            new_books_query_set[count]['current_price'] = book.current_price
            if book.previous_price is not None:
                percent = calc_percent(book.current_price, book.previous_price)
                new_books_query_set[count]['sale_percent'] = percent
                new_books_query_set[count]['previous_price'] = book.previous_price
            new_books_query_set[count]['date_create'] = book.date_create
            new_books_query_set[count]['description'] = book.description
            book_genre = str(book.book_genre)
            book_genre = book_genre.split(";")
            book_genre.sort(key=len)
            book_genre.reverse()
            new_books_query_set[count]['book_genre'] = book_genre
            count += 1

    elif not all:
        proper_query_set = books_query_set
        new_books_query_set = [{} for _ in range(len(proper_query_set))]
        count = 0
        for book in proper_query_set:
            for b in book:
                new_books_query_set[count]['book_id'] = b.pk
                new_books_query_set[count]['book_name'] = b.book_name
                new_books_query_set[count]['book_slug'] = b.book_slug
                new_books_query_set[count]['book_img'] = b.book_img
                new_books_query_set[count]['book_category'] = b.book_category
                new_books_query_set[count]['current_price'] = b.current_price
                print(b.previous_price, '<-- previous_price')
                if b.previous_price is not None:
                    percent = calc_percent(b.current_price, b.previous_price)
                    new_books_query_set[count]['previous_price'] = b.previous_price
                    new_books_query_set[count]['sale_percent'] = round(percent)
                new_books_query_set[count]['date_create'] = b.date_create
                new_books_query_set[count]['description'] = b.description
                book_genre = str(b.book_genre)
                book_genre = book_genre.split(";")
                book_genre.sort(key=len)
                book_genre.reverse()
                new_books_query_set[count]['book_genre'] = book_genre
                count += 1

    return new_books_query_set



















def csrf_failure(request, reason=""):
    return HttpResponse('<h1>Ты здесь потому, что хозяин этого сайта наложал!!!</h1>')