from django.shortcuts import render
from .models import Student
# from .serializers import StudentSerializer
from . import serializers
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
from rest_framework.decorators import api_view
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


@api_view(['GET'])
def student(request):
    student = Student.objects.all()
    print(student)
    serializer = serializers.StudentSerializer(student, many = True)
    # print(serializer.data)
    # json_data = JSONRenderer().render(serializer.data)
    # print(json_data)
    # return HttpResponse(json_data, content_type='application/json')
    # return JsonResponse(serializer.data, safe=False)
    return Response(serializer.data)

@api_view(['GET'])
def student_detail(request,pk):
    id = request.data.get(pk)
    print("id",id)
    student = Student.objects.get(id=pk)
    print(student)
    serializer = serializers.StudentSerializer(student)
    # print(serializer.data)
    # json_data = JSONRenderer().render(serializer.data)
    # print(json_data)
    # return HttpResponse(json_data, content_type='application/json')
    return Response(serializer.data)


@api_view(['POST'])
# @csrf_exempt
def student_create(request):
    if request.method == 'POST':
        json_data = request.body
        print(json_data)
        # stream = io.BytesIO(json_data)  //string
        # print("stream",stream)
        # pythondata = JSONParser().parse(stream)  //json
        # print("pythondata",pythondata)
        print("request.data",request.data)
        # print("request.body",request.body)
        serializer = serializers.StudentSerializer(data=request.data)
        print("serializer",serializer)
        if serializer.is_valid():
            serializer.save()
            res = {'message': 'Student created successfully'}
            # json_data = JSONRenderer().render(res)
            # return HttpResponse(json_data, content_type='application/json')
            return Response (res)

        # json_data = JSONRenderer().render(serializer.errors)
        # return HttpResponse(json_data, content_type='application/json')    
        return Response(serializer.errors)

            # return JsonResponse(serializer.data, status=201)

    # serializer = serializers.StudentSerializer(data=request.data)
    # if serializer.is_valid():
    #     serializer.save()
    #     return JsonResponse(serializer.data, status=201)



@api_view(['PUT'])
def student_update(request,pk):
    student = Student.objects.get(id=pk)
    print(student)
    serializer = serializers.StudentSerializer(student,data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message':f'{student} is updated !!'})
    return Response(serializer.errors)

@api_view(['DELETE'])
def student_delete(request,pk):
    student = Student.objects.get(pk=pk)
    student.delete()
    return Response({'message':f'{pk} -- deleted !!'},status=status.HTTP_204_NO_CONTENT)
