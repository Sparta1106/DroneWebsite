from django.shortcuts import render

# Create your views here.

# Calls(Render) the html file(template) located in templates/dashboard.html
def home_view(request):
    return render(request, 'dashboard.html')