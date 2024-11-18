from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
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
    permission_classes = [AllowAny]  #Разрешаем доступ всем


class CreateTaleView(APIView):
    def post(self, request):
        serializer = TalesSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
