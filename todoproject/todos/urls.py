from django.urls import path
from .views import get_todos, add_todo, update_todo, delete_todo, api_root

urlpatterns = [
    path('', api_root, name='api_root'),  # Add this line
    path('todos/', get_todos, name='get_todos'),
    path('todos/add/', add_todo, name='add_todo'),
    path('todos/update/<int:pk>/', update_todo, name='update_todo'),
    path('todos/delete/<int:pk>/', delete_todo, name='delete_todo'),
]
