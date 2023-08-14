from django.db import models
from test_project.settings import MEDIA_ROOT


class Book(models.Model):
    book_slug = models.SlugField(max_length=65, unique=True, db_index=True, verbose_name="Slug-URL for book")
    book_name = models.CharField(max_length=50, verbose_name='Название книги:')
    book_img = models.ImageField(
        upload_to=MEDIA_ROOT + '/' + 'dir_for_BOOKS_IMAGES/',
        verbose_name='Изображение:', max_length=255)
    current_price = models.IntegerField(verbose_name='Цена текущая(со скидкой):')
    previous_price = models.IntegerField(blank=True, null=True, verbose_name='Цена без скидки:')
    # book_author = models.ForeignKey('Author', on_delete=models.CASCADE, verbose_name='Автор книги')
    book_category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Категория книги:')
    # book_genre = models.ForeignKey('Genre', on_delete=models.CASCADE, verbose_name='Жанр книги')
    book_genre = models.TextField(max_length=65, verbose_name="Жанр(ы):")
    description = models.TextField(verbose_name='Описание книги:')
    date_create = models.DateField(verbose_name='Дата издания книги:')

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return self.book_name


class Category(models.Model):
    id = models.IntegerField(primary_key=True, blank=True)
    category_slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="Slug-URL for category")
    category_img = models.ImageField(
        upload_to=MEDIA_ROOT + '/' + 'dir_for_CATEGORIES_IMAGES/',
        verbose_name='Изображение категории', max_length=255)
    category_name = models.CharField(max_length=55, verbose_name='Название категории')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.category_name


# class Genre(models.Model):
#     id = models.IntegerField(primary_key=True, blank=True)
#     genre_slug = models.SlugField(max_length=65, unique=True, db_index=True, verbose_name="Slug-URL for genre")
#     genre_img = models.ImageField(
#         upload_to=MEDIA_ROOT + '/' + 'dir_for_GENRES_IMAGES/',
#         verbose_name='Изображение жанра', max_length=255)
#     genre_name = models.CharField(max_length=55, verbose_name='Название жанра')
#
#     class Meta:
#         verbose_name = 'Жанр'
#         verbose_name_plural = 'Жанр'
#
#     def __str__(self):
#         return self.genre_name


# class Author(models.Model):
#     author_slug = models.SlugField(max_length=65, unique=True, db_index=True, verbose_name="Slug-URL for author")
#     author_img = models.ImageField(upload_to=MEDIA_ROOT + '/' + 'dir_for_AUTHORS_IMAGES/', max_length=255)
#     first_name = models.CharField(max_length=55)
#     surname = models.CharField(max_length=55)
#     last_name = models.CharField(max_length=55)
#     date_born = models.DateField()
#     date_death = models.DateField()
#     description = models.TextField()
#
#     class Meta:
#         verbose_name = 'Автор'
#         verbose_name_plural = 'Писатели'
#
#     def __str__(self):
#         return [self.first_name,
#                 self.surname,
#                 self.last_name]




