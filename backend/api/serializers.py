import django
from django.utils import timezone
from django.utils.functional import empty
from rest_framework import serializers
from rest_framework.relations import HyperlinkedRelatedField
from rest_framework.utils import serializer_helpers

from .models import User, TodoList, TodoItem
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    # url=serializers.HyperlinkedIdentityField(view_name='user-detail')
    class Meta:
        model=User
        fields=('username',
                'password',
                'first_name',
                'last_name',
                'email')

class UserListSerializer(serializers.ModelSerializer):
    # url=serializers.HyperlinkedIdentityField(view_name='users-detail')
    class Meta:
        model=User
        fields=('id',
                'username',
                'first_name',
                'last_name',
                'email')

class UserCreateSerializer(serializers.ModelSerializer):

    def create(self, validated_data):    
        if validated_data.get('password'):
            validated_data['password'] = make_password(
                validated_data['password']
            )
        user = get_user_model().objects.create(**validated_data)

        return user

    class Meta:
        model=User
        fields=('username',
                'first_name',
                'last_name',
                'password',
                'email')

class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('username',
                'first_name',
                'last_name',
                'email')

class TodoItemSerializer(serializers.HyperlinkedModelSerializer):
    # list = TodoListSerializer()
    url=serializers.HyperlinkedIdentityField(view_name='list-items-detail')
    list=HyperlinkedRelatedField(read_only=True,view_name='lists-detail')
    class Meta:
        model=TodoItem
        fields=('__all__')

class TodoItemCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model=TodoItem
        fields=('__all__')

class TodoItemUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model=TodoItem
        fields=('__all__')

class TodoItemListSerializer(serializers.HyperlinkedModelSerializer):
    url=serializers.HyperlinkedIdentityField(view_name='list-items-detail')
    class Meta:
        model=TodoItem
        fields=('id','url','title', 'description', 'finished')

class TodoListSerializer(serializers.HyperlinkedModelSerializer):
    url=serializers.HyperlinkedIdentityField(view_name='lists-detail')
    user = UserListSerializer()
    list_items = TodoItemListSerializer(many=True, read_only=True)
    class Meta:
        model=TodoList
        fields=('__all__')

class TodoListCreateSerializer(serializers.ModelSerializer):
    list_items = TodoItemListSerializer(many=True, default=[])
    
    # Override create action
    def create(self, validated_data):
        items_data = validated_data.pop('list_items')
        new_list = TodoList.objects.create(**validated_data)
        for item_data in items_data:
            TodoItem.objects.create(list=new_list,**item_data)
        return new_list

    class Meta:
        model=TodoList
        fields=('__all__')

class TodoListUpdateSerializer(serializers.ModelSerializer):
    # list_items = TodoItemListSerializer(many=True, read_only=True, default=[])
    class Meta:
        model=TodoList
        fields=('__all__')
