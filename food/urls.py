from django.contrib import admin
from .models import *
from django.urls import path
from .views import home


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
]
