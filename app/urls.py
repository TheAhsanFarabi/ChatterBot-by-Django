# app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Basic route to a view named index
]
