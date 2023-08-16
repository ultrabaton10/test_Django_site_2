from django.urls import path, re_path
from .views import *


urlpatterns = [
    path('', App1Home.as_view(), name="index"),
    path('chosen-book/<slug:book_slug>/<int:book_id>/', chosen_book, name="chosen-book"),
    path('log_in', log_in, name="log_in"),
    path('log_out', RegisterUser.as_view(), name="log_out")
    # path('categories', categories, name="categories"),
    # path('books-by-category', books_by_category, name="books_by_category"),
    # path('create-new-product', BookCreateView.as_view(), name="create"),
]
