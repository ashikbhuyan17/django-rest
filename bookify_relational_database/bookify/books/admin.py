from django.contrib import admin

from books.models import BookList,SellingPlatform,Review

admin.site.register(BookList)
admin.site.register(SellingPlatform)
admin.site.register(Review)