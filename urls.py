from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('modules/', views.list_modules, name='list_modules'),
    path('modules/<int:module_id>/', views.module_details, name='module_details'),
    path('registration/', views.registration, name='registration'),
]

