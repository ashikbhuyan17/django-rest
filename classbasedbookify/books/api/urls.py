# from django.urls import path
# from books.api import views

# urlpatterns = [
#     path('',views.book_list)
# ]

from django.urls import path

from . import views

urlpatterns = [
    path('list',views.BooksList.as_view(),name='book-list'),
    path('list/<int:pk>',views.BookDetails.as_view(),name='book-detail'),
]