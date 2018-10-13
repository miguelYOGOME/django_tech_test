from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import generics

from .serializers import LineSerializer, RouteSerializer
from .models import LineModel, RouteModel
from .schemas import LinesSchema

# Create your views here.

class LinesList(generics.ListCreateAPIView):
    queryset = LineModel.objects.all()
    schema_class = LinesSchema
    serializer_class = LineSerializer

class LineDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = LineModel.objects.all()
    schema_class = LinesSchema
    serializer_class = LineSerializer

class RouteList(generics.ListCreateAPIView):
    queryset = RouteModel.objects.all()
    serializer_class = RouteSerializer

class RouteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = RouteModel.objects.all()
    serializer_class = RouteSerializer