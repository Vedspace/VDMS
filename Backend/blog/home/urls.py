from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
path('', views.home,name='Home'),
path('about', views.about,name="Aboutus"),
path('contact', views.contact,name="Contact"),
path('search', views.search, name="Search"),
]

