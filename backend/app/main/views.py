from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import *


class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class GroupViewSet(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

