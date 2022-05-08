# import books import models
from books import models
from rest_framework.response import Response
from . import serilizers
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
# @api_view(['GET'])
# def books_list(request):
#     books = models.Books.objects.all()
#     serializer = serilizers.BookSerializer(books, many=True)
#     return Response(serializer.data)

class BooksList(APIView):
    def get(self,request):
        books = models.Books.objects.all()
        serializer = serilizers.BookSerializer(books, many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = serilizers.BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    

class BookDetails(APIView):

    def get_object(self, pk):
        try:
            return models.Books.objects.get(pk=pk)
        except models.Books.DoesNotExist:
            raise Http404

    def get(self,request,pk):
        book = models.Books.objects.get(pk=pk)
        serializer = serilizers.BookSerializer(book)
        return Response(serializer.data)

    def put(self,request,pk):
        # book = models.Books.objects.get(pk=pk)
        transformer = self.get_object(pk)
        serializer=serilizers.BookSerializer(transformer,data=request.data)
        if serializer.is_valid():
            serializer.save() 
            return Response(serializer.data)     
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)        

    def patch(self, request, pk):
        transformer = self.get_object(pk)
        serializer = serilizers.BookSerializer(transformer,
                                           data=request.data,
                                           partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
          

    def delete(self,request,pk):
        # book = models.Books.objects.get(pk=pk)
        # book.delete()
        transformer = self.get_object(pk)
        transformer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)        