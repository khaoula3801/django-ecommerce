from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('cart/', views.cart, name='cart'),
    path('cart/add/<int:id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:id>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/decrease/<int:id>/', views.decrease_quantity, name='decrease_quantity'),
    path('cart/increase/<int:id>/', views.increase_quantity, name='increase_quantity'),
    path('categories/', views.category_list, name='category_list'),
    path('categories/<int:id>/', views.category_detail, name='category_detail'),
    path('<int:id>/', views.product_detail, name='product_detail'),
]
