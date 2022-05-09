from functools import partial
from django.shortcuts import render
from rest_framework.response import Response
from yaml import serialize
from .models import Students
from .serializers import StudentSerializrer
from rest_framework import status
from rest_framework import viewsets

from students import serializers
# Create your views here.
class StudentViewSet(viewsets.ViewSet):
    def list(self,request):
        stu = Students.objects.all()
        serialize = StudentSerializrer(stu,many=True)
        return Response(serialize.data)


    def retrieve(self, request, pk=None):
        queryset = Students.objects.get(pk=pk)
        serializer = StudentSerializrer(queryset)
        return Response(serializer.data)    


    def create(self, request):
        serializer = StudentSerializrer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


    def update(self, request, pk=None):
        queryset = Students.objects.get(pk=pk)
        serializer = StudentSerializrer(queryset, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)  

    def partial_update(self, request, pk=None):
        queryset = Students.objects.get(pk=pk)
        serializer = StudentSerializrer(queryset, request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)        


    def destroy(self, request, pk=None):
        queryset = Students.objects.get(pk=pk)
        queryset.delete()
        return Response({'msg':'delete success'})
        