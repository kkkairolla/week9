from django.urls import path

from . import views

urlpatterns = [
    path('categories/', views.category_list, name='category_list'),
    path('products/', views.product_list1),
    path('products/<int:product_id>/', views.product_detail),
    path('categories/<int:category_id>/', views.category_detail),
    path('categories/<int:category_id>/products/', views.product_list2)

]