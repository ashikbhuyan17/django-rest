from atexit import register
from django.contrib import admin
from .models import Student
from django.contrib import admin
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'city', 'roll', 'passby']
    ordering = ['name']

admin.site.register(Student, StudentAdmin)
