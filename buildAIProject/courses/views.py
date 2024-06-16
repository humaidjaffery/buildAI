from django.shortcuts import render, HttpResponse
from django.template import loader

# Create your views here.
def coursesPage(request, course, module):
    context = {
        "course": course,
        "module": module
    }
    return render(request, 'courses.html', context)