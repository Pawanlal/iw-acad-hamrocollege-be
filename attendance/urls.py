from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import AttendanceModelViewSet

r = DefaultRouter()
r.register('attendancesheet',AttendanceModelViewSet)

app_name = 'attendance'
urlpatterns = [

]+r.urls