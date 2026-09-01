# my_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Accessing http://127.0.0 triggers the view
    path('about/', views.about, name='about'),
    path('faqs/', views.FAQs, name='faqs'),

]
