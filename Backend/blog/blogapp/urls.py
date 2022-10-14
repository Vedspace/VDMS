from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
path('', views.home,name='blogHome'),
path('<str:slug>', views.blogPost,name='blogPost'),


]