from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Создаем роутер и регистрируем ViewSet'ы
router = DefaultRouter()
router.register(r'students', views.StudentViewSet, basename='student')
router.register(r'group', views.GroupViewSet, basename='group')

# Включаем маршруты, созданные роутером, в основной urlpatterns
urlpatterns = [
    path('', include(router.urls)),
]