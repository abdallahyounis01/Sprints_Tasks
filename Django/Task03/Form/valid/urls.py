from django.urls import path
from django.urls import include
from django.contrib import admin
from . import views
from django.shortcuts import HttpResponse

urlpatterns = [

    path('view/', views.home, name='view'),
]
