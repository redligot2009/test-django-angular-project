from django.urls import include, path
from rest_framework import routers
from .views import UserViewSet, TodoListViewSet, TodoItemViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename='users')
router.register(r'lists', TodoListViewSet, basename='lists')
router.register(r'list-items', TodoItemViewSet, basename='list-items')

urlpatterns = [
    path('api/',include(router.urls)),
    path('api-auth/',include('rest_framework.urls',namespace='rest_framework')),
]