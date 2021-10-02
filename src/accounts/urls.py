from os import name
from django.contrib import admin
from django.urls import path
from django.urls.conf import re_path

from pages.views import home_view
from . import views

urlpatterns = [
    path('products/', views.products),
    path('customer/', views.customer),
    path('aboutus/', views.aboutus)
    
]
