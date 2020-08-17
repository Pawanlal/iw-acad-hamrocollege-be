from django.contrib import admin

from .models import Classroom, ClassroomMember, ClassroomDiscussion

admin.site.register(Classroom)
admin.site.register(ClassroomMember)
admin.site.register(ClassroomDiscussion)