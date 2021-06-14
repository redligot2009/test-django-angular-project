from django.urls import include, path
from rest_framework import routers
from .views import TodoListViewSet, TodoItemViewSet
from djoser import views as djoser_views
from rest_framework_simplejwt import views as jwt_views

router = routers.DefaultRouter()
# router.register(r'users', UserViewSet, basename='users')
router.register(r'lists', TodoListViewSet, basename='lists')
router.register(r'list-items', TodoItemViewSet, basename='list-items')

urlpatterns = [
    path('api/',include(router.urls)),
    path('api-auth/',include('rest_framework.urls',namespace='rest_framework')),
    path('api/auth/', include('djoser.urls')),
    path('api/auth/', include('djoser.urls.jwt')),
]