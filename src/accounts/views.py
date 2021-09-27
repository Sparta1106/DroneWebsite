from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# Calls(Render) the html file(template) located in templates/accounts/dashboard.html
def home(request):
    return render(request, 'accounts/dashboard.html')

# Calls(Render) the html file(template) located in templates/accounts/products.html
def products(request):
    return render(request, 'accounts/products.html')

# Calls(Render) the html file(template) located in templates/accounts/customer.html
def customer(request):
    return render(request, 'accounts/customer.html' )

