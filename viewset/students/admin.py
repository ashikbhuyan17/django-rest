from django.contrib import admin

# Register your models here.
from .models import Students
admin.site.register(Students)
# @admin.register(Student)
# class StudentAdmin(admin.ModelAdmin):
#     list_display = ('name', 'roll', 'city')