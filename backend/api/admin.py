from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.

from .models import User, TodoList, TodoItem

admin.site.register(User, UserAdmin)
admin.site.register(TodoList)
admin.site.register(TodoItem)