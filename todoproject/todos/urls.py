from django.urls import path
from .views import get_todos, add_todo, update_todo, delete_todo, api_root

urlpatterns = [
    path('', get_todos, name='get_todos'),
    path('add/', add_todo, name='add_todo'),
    path('update/<int:pk>/', update_todo, name='update_todo'),
    path('delete/<int:pk>/', delete_todo, name='delete_todo'),
]
