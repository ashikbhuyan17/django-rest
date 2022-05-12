from django.contrib import admin

from books.models import BookList,SellingPlatform

admin.site.register(BookList)
admin.site.register(SellingPlatform)