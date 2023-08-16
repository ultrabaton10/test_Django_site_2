from .models import Category

header_menu = [
    {'url_name': 'index', 'title': 'Book Shop'},
]

categories_dct = {
    'detective': 1,
    'fantasy': 2,
    'business-literature': 3,
    'for-little-ones': 4,
    'thriller': 5
}

std_media_url = '../media/'


class DataMixin():
    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Category.objects.all()
        context['menu'] = header_menu
        context['cats_dct'] = categories_dct

        return context
