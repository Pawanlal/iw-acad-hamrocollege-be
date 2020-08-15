  
from django.contrib import admin

from .models import SemesterList,Faculty,SubjectList

admin.site.register(SemesterList)
admin.site.register(SubjectList)
admin.site.register(Faculty)
