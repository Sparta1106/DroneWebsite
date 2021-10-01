from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.products),
    path('customer/', views.customer),
    
]
