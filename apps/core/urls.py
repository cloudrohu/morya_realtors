# my_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
  
    path('about/', views.about, name='about'),
    path('faqs/', views.FAQs, name='faqs'),
    path('developers/', views.developers, name='developers'),
    path('localities/', views.localities, name='localities'),
    path('services/', views.services, name='services'),
    path('calculator/', views.Calculator, name='calculator'),

]
