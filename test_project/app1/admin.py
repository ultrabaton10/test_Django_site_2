from django.contrib import admin
from .models import Book, Category


# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ['book_category', 'book_name', 'current_price']
    list_filter = ['current_price', 'book_name', 'book_category', 'book_slug']
    search_fields = ['book_category']
    prepopulated_fields = {"book_slug": ("book_name",)}
    # fields = ['book_name', 'current_price']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'category_img', 'category_name', 'category_slug']
    list_filter = ['category_name', 'category_slug', 'id']

admin.site.register(Book, BookAdmin)
admin.site.register(Category, CategoryAdmin)
