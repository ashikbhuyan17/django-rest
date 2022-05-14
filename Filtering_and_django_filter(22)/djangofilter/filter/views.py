from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

# Create your views here.


class StudentListView(ListAPIView):
    student = Student.objects.all()
    serializer_class = StudentSerializer
    # filter_backends = [DjangoFilterBackend]
    filterset_fields = ['city','name']

    def get_queryset(self):
        return Student.objects.order_by('name')


