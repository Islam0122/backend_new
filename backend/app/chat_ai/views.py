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


class TalesModelViewSet(ModelViewSet):
    queryset = Tales.objects.all()
    serializer_class = TalesSerializer
    permission_classes = [AllowAny]

