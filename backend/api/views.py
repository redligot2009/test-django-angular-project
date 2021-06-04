from django.shortcuts import render

from rest_framework import viewsets

from .models import User, TodoList, TodoItem
from .serializers import UserSerializer, TodoListSerializer, TodoItemSerializer

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer

class TodoListViewSet(viewsets.ModelViewSet):
    queryset=TodoList.objects.all()
    serializer_class=TodoListSerializer

class TodoItemViewSet(viewsets.ModelViewSet):
    queryset=TodoItem.objects.all()
    serializer_class=TodoItemSerializer
