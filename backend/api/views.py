from django.shortcuts import render

from rest_framework import viewsets, permissions

from .models import User, TodoList, TodoItem
from .serializers import TodoItemCreateSerializer, TodoItemListSerializer, TodoItemUpdateSerializer, TodoListCreateSerializer, TodoListUpdateSerializer, UserCreateSerializer, UserListSerializer, UserSerializer, TodoListSerializer, TodoItemSerializer, UserUpdateSerializer

# Create your views here.

# class UserViewSet(viewsets.ModelViewSet):
#     queryset=User.objects.all()
#     def get_serializer_class(self):
#         if(self.action=='list'):
#             return UserListSerializer
#         elif(self.action=='retrieve'):
#             return UserSerializer
#         elif(self.action=='update'):
#             return UserUpdateSerializer
#         else:
#             return UserCreateSerializer

class TodoListViewSet(viewsets.ModelViewSet):
    queryset=TodoList.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    def get_serializer_class(self):
        if(self.action=='list'):
            return TodoListSerializer
        elif(self.action=='retrieve'):
            return TodoListSerializer
        elif(self.action=='update'):
            return TodoListUpdateSerializer
        else:
            return TodoListCreateSerializer

class TodoItemViewSet(viewsets.ModelViewSet):
    queryset=TodoItem.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    def get_serializer_class(self):
        if(self.action=='list'):
            return TodoItemListSerializer
        elif(self.action=='retrieve'):
            return TodoItemSerializer
        elif(self.action=='update'):
            return TodoItemUpdateSerializer
        else:
            return TodoItemCreateSerializer
