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
    path('contact/', views.Contact, name='contact'),
    path('privacy-policy/', views.Privacy_Policy, name='privacy_policy'),
    path('terms-of-service/', views.terms_of_service, name='terms_of_service'),
    path('disclaimer/', views.disclaimer, name='disclaimer'),
    path('thank-you/', views.thank_you, name='thank_you'),



]
