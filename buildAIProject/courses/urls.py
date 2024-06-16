from django.urls import path
from . import views

urlpatterns = [
    path('<str:course>/<int:module>', views.coursesPage)
]