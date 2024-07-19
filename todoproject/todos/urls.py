from django.urls import path
from .views import get_todos, add_todo, update_todo, delete_todo

urlpatterns = [
    path('todos/', get_todos, name='get_todos'),
    path('todos/add/', add_todo, name='add_todo'),
    path('todos/update/<int:pk>/', update_todo, name='update_todo'),
    path('todos/delete/<int:pk>/', delete_todo, name='delete_todo'),
]
