from django.urls import path, re_path
from .views import *


urlpatterns = [
    path('', index, name="index"),
    path('chosen-book/<slug:book_slug>/<int:book_id>/', chosen_book, name="chosen-book"),
    # path('categories', categories, name="categories"),
    # path('books-by-category', books_by_category, name="books_by_category"),
    # path('create-new-product', BookCreateView.as_view(), name="create"),
]
