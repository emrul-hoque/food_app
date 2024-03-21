from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('place_order/', views.place_order, name='place_order'),
    path('about_us/', views.about_us, name='about_us'),
]

