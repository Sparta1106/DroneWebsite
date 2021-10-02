from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# Calls(Render) the html file(template) located in templates/products.html
def products(request):
    return render(request, 'products.html')

# Calls(Render) the html file(template) located in templates/customer.html
def customer(request):
    return render(request, 'customer.html' )

