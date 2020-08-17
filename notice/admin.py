from django.contrib import admin

from .models import Notice, Comment, Category

admin.site.register(Category)
admin.site.register(Notice)
admin.site.register(Comment)
