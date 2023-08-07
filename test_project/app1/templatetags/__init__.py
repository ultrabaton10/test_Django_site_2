from django.template import Library


register = Library()

register.inclusion_tag('app1/show_header_menu.html')
def show_header_menu():
    context = {}
    return context