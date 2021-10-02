from os import name
from django.contrib import admin
from django.urls import path
from django.urls.conf import re_path

from pages.views import home_view
from . import views

urlpatterns = [
    path('', views.home_view, name='home-page'),
    path('products', views.products, name='products-page'),
    path('customer', views.customer, name='customer-page'),

    #path('products/', views.products, name='produc-page'),
    #path('customer/', views.customer, name='customer-page'),
    #re_path('#', views.dashboard),    
    #path('products/', views.products),
    #path('customer/', views.customer),
    
]
