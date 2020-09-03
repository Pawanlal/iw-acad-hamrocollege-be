from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import FacultyModelViewSet, SubjectListModelViewSet, SemesterListModelViewSet, SectionModelViewSet

r = DefaultRouter()
r.register('faculty', FacultyModelViewSet)
r.register('subjectlist', SubjectListModelViewSet)
r.register('semesterlist', SemesterListModelViewSet)
r.register('section', SectionModelViewSet)

app_name = 'college'
urlpatterns = [
    
] + r.urls