from django.urls import path
from . import views
# urlpatterns = [
#     path('student',views.StudentViewSet.as_view())
# ]

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'students', views.StudentViewSet, basename='user')
urlpatterns = router.urls
