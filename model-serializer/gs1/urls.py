
from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student-create/', views.student_create),
    path('student/', views.student),
    path('student-update/<int:pk>/', views.student_update),
    path('student-delete/<int:pk>/', views.student_delete),
    path('student/<int:pk>/', views.student_detail),
]
