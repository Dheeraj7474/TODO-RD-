from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import TodoItem
from .serializers import TodoItemSerializer

from rest_framework.reverse import reverse

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'todos': reverse('get_todos', request=request, format=format),
    })
    
@api_view(['GET'])
def get_todos(request):
    todos = TodoItem.objects.all()
    serializer = TodoItemSerializer(todos, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def add_todo(request):
    serializer = TodoItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['PUT'])
def update_todo(request, pk):
    todo = TodoItem.objects.get(id=pk)
    serializer = TodoItemSerializer(todo, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def delete_todo(request, pk):
    todo = TodoItem.objects.get(id=pk)
    todo.delete()
    return Response(status=204)
