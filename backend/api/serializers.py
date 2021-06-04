import django
from django.utils import timezone
from django.utils.functional import empty
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.utils import serializer_helpers

from .models import User, TodoList, TodoItem

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('__all__')

class TodoListSerializer(serializers.ModelSerializer):
    class Meta:
        model=TodoList
        fields=('__all__')

class TodoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=TodoItem
        fields=('__all__')