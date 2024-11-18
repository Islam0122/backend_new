from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
from .serializers import *


class TopTalesListView(ListAPIView):
    queryset = TopTales.objects.all()
    serializer_class = TopTalesSerializer
    permission_classes = [AllowAny]


class TopTalesDetailView(RetrieveAPIView):
    queryset = TopTales.objects.all()
    serializer_class = TopTalesSerializer
    lookup_field = 'pk'
    permission_classes = [AllowAny]


class TalesViewSet(ModelViewSet):
    queryset = Tales.objects.all()
    serializer_class = TalesSerializer
    permission_classes = [AllowAny]  # Разрешаем доступ всем

    def perform_create(self, serializer):
        """
        Обрабатываем создание объекта.
        Если пользователь анонимный, поле `user` остается пустым.
        """
        user = self.request.user
        if user.is_authenticated:
            serializer.save(user=user)  # Привязываем пользователя
        else:
            serializer.save()
