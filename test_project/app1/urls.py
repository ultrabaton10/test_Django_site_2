from django.urls import path, re_path
from .views import *

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', index, name="index"),
    path('products', products, name="products"),
    # re_path('category/<slug:cat_id>/', products_by_category, name="redirect_to_products_by_chosen_category"),
    path('categories', categories, name="categories"),
    path('category/<slug:cat_id>/', products_by_category, name="products_by_category"),
    path('create-new-product', ProductCreateView.as_view(), name="create"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)