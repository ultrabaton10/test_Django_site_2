from django.forms import ModelForm
from .models import Products


class ProductForm(ModelForm):
    '''
    Класс формы - ProductForm является производным
    от базового класса ModelForm из модуля django.forms.

    '''
    class Meta:
        model = Products
        fields = ('image',
                  'name',
                  'author',
                  'category',
                  'price')


