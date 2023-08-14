from django import template


register = template.Library()


filters_dct = {
    'detective': '1',
    'fantasy': '2',
    'business-literature': '3',
    'for-little-ones': '4',
    'thriller': '5'
}

@register.inclusion_tag('app1/show_header_menu.html')
def show_menu_bar(header_menu : list[{str: str}],
                  title : str,
                  make_books_text_active : bool):
    context = {
        'header_menu': header_menu,
        'title': title,
        'make_books_text_active': make_books_text_active
    }

    return context



@register.inclusion_tag('app1/show_filter_zone.html')
def show_filter_zone():
    context = {
        'filters_dct': filters_dct
    }
    return context

