from jinja2 import Template


header_menu = [
    {'url' : "{% url 'index' %}", 'title' : 'Book Shop'},
    {'url' : "{% url 'products_by_category' cat_id='0' %}", 'title' : 'Products'},
    {'url' : "{% url 'categories' %}", 'title' : 'Categories'},
    {'url' : "{% url 'create' %}", 'title' : 'Create'},
]

title = 'Book Shop'

list = '''
Some text 
{% for i in header_menu %}
    <div>
    Hell
    {% if i['title'] == 'Book Shop' %}
        {{ i['title'] }}
    {% endif %} 
</div>
{% endfor %}
'''

tm = Template(list)
show = tm.render(header_menu=header_menu)
print(show)