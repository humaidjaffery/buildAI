from django.shortcuts import render, HttpResponse
from django.template import loader

# Create your views here.
def home(request):
    print(request)
    home_template = loader.get_template('home.html')
    return HttpResponse(home_template.render())