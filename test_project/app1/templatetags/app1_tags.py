from django import template


register = template.Library()


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





