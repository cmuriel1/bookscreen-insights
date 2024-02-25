from django.urls import path

from . import views


app_name = 'products'

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search, name='search'),
    path('product/<str:slug>', views.product_details, name="details"),
    path('product/type/<str:slug>', views.product_search_categories, name="cate_filter")
]
