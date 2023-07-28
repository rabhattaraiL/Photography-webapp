from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('service/', views.service, name='blog-service'),
    path('gallery/', views.gallery, name='blog-gallery'),
    path('contact/', views.contact, name= 'blog-contact'),
]