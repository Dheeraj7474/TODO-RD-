# todoproject/urls.py
from django.contrib import admin
from django.urls import path, include
from . import views  # Import your views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('todos.urls')),
    path('', views.home, name='home'),  # Add this line
]
