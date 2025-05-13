from django.urls import path
from .views import shop, product_detail ,category
urlpatterns = [
    path('', shop, name='shop'),
    path('product_detail/<int:product_id>/', product_detail, name='product_detail'),
    path('category/<str:category_name>/', category, name='category' ),
]