from django.contrib import admin

# Register your models here.
from .models import Announcement, Club, Member

admin.site.register(Announcement)
admin.site.register(Club)
admin.site.register(Member)


