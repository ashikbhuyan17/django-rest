from django.urls import path

from . import views

urlpatterns = [
    # path('list',views.books_list,name='book-list'),
    # path('<int:pk>',views.book_details,name='book-details')
    path('list',views.BookList.as_view(),name='book-list'),
    path('<int:pk>',views.BookDetailsView.as_view(),name='book-details'),
    path('platform',views.SellingPlatformList.as_view(),name='platform-list'),
    path('platform/<int:pk>',views.SellingPlatformDetailsView.as_view(),name='platform-details'),
    path('review/',views.ReviewList.as_view(),name='review-list'),

]