from django.urls import path

from . import views

urlpatterns = [
    path('list',views.books_list,name='book-list'),
    path('<int:pk>',views.book_details,name='book-details')
]