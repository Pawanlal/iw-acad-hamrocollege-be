  
from django.contrib import admin

from .models import SemesterList, Faculty, SubjectList, Section

admin.site.register(SemesterList)
admin.site.register(SubjectList)
admin.site.register(Faculty)
admin.site.register(Section)
