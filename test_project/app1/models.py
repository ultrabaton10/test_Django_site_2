from django.db import models
from test_project.settings import MEDIA_ROOT


class Products(models.Model):
    id = models.IntegerField(primary_key=True)
    image = models.ImageField(upload_to=MEDIA_ROOT, verbose_name='изображение', null=True, blank=True)
    name = models.CharField(max_length=50, blank=False, verbose_name='название')
    author = models.CharField(max_length=50, blank=False, verbose_name='автор')
    category = models.ForeignKey('Category', verbose_name='категория', on_delete=models.PROTECT, null=True)
    price = models.IntegerField(verbose_name='цена')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Category(models.Model):
    id = models.IntegerField(primary_key=True)
    image = models.ImageField(upload_to=MEDIA_ROOT, verbose_name='изображение', null=True, blank=True)
    name = models.CharField(max_length=50, blank=False, verbose_name='название категории')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


