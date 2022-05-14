
from django.urls import path
from . import views
urlpatterns = [
    path('stu/',views.StudentListView.as_view(),),
]
