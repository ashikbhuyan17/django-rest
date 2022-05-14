from platform import platform
from re import S
from books.api.serializers import BooksSerializer,SellingPlatformSerializer
from rest_framework.response import Response
# from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status

from books import models

class BookList(APIView):

    def get(self,request):
        books = models.BookList.objects.all()
        serializer = BooksSerializer(books,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        # print("/////////////////",request.data)
        # print(request.data['title'])
        # print(request.data.get('title'))
        serializer = BooksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors)


class BookDetailsView(APIView):

    def get(self,request,pk):
        try:
            book = models.Books.objects.get(pk=pk)
        except models.Books.DoesNotExist:
            return Response({'error':'object not found !!'},
            status=status.HTTP_404_NOT_FOUND)
        serializer = BooksSerializer(book)
        return Response(serializer.data)
    
    def put(self,request,pk):
        book = models.Books.objects.get(pk=pk)
        serializer = BooksSerializer(book,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':f'{book} is updated !!'})
        return Response(serializer.errors)

    def delete(self,request,pk):
        book = models.Books.objects.get(pk=pk)
        book.delete()
        return Response({'message':f'{pk} -- deleted !!'},status=status.HTTP_204_NO_CONTENT)


class SellingPlatformList(APIView):

    def get(self,request):
        platform = models.SellingPlatform.objects.all()
        serializer = SellingPlatformSerializer(platform,many=True,context={'request': request})
        return Response(serializer.data)
    
    def post(self,request):
        serializer = SellingPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors)

class SellingPlatformDetailsView(APIView):

    def get(self,request,pk):
        try:
            platform = models.SellingPlatform.objects.get(pk=pk)
        except models.SellingPlatform.DoesNotExist:
            return Response({'error':'object not found !!'},
            status=status.HTTP_404_NOT_FOUND)
        serializer = SellingPlatformSerializer(platform)
        return Response(serializer.data)
    
    def put(self,request,pk):
        platform = models.SellingPlatform.objects.get(pk=pk)
        serializer = SellingPlatformSerializer(platform,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':f'{platform} is updated !!'})
        return Response(serializer.errors)

    def delete(self,request,pk):
        platform = models.SellingPlatform.objects.get(pk=pk)
        platform.delete()
        return Response({'message':f'{pk} -- deleted !!'},status=status.HTTP_204_NO_CONTENT)



# @api_view(['GET','POST'])
# def books_list(request):
#     if request.method == 'GET':
#         books = models.Books.objects.all()
#         serializer = BooksSerializer(books,many=True)
#         return Response(serializer.data)

#     if request.method == 'POST':
#         print('request data',request.data)
#         serializer = BooksSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)


# @api_view(['GET','PUT','DELETE'])
# def book_details(request,pk):
#     if request.method == 'GET':
#         try:
#             book = models.Books.objects.get(pk=pk)
#         except models.Books.DoesNotExist:
#             return Response({'error':'object not found !!'},
#             status=status.HTTP_404_NOT_FOUND)
#         serializer = BooksSerializer(book)
#         return Response(serializer.data)

#     if request.method == 'PUT':
#         book = models.Books.objects.get(pk=pk)
#         serializer = BooksSerializer(book,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'message':f'{book} is updated !!'})
#         return Response(serializer.errors)
    
#     if request.method == 'DELETE':
#         book = models.Books.objects.get(pk=pk)
#         book.delete()
#         return Response({'message':f'{pk} -- deleted !!'},status=status.HTTP_204_NO_CONTENT)






        




