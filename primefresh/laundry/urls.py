from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('services/', views.services, name='services'),
    path('booking/', views.booking, name='booking'),
    path('booking/success/<int:pk>/', views.booking_success, name='booking_success'),
    path('gallery/', views.gallery, name='gallery'),
    path('contact/', views.contact, name='contact'),
]
