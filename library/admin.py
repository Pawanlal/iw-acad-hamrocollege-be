from django.contrib import admin

# Register your models here.
from .models import Book, Author, Publisher,BookRequest,BookIssue,Fine

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(BookIssue)
admin.site.register(Publisher)
admin.site.register(BookRequest)
admin.site.register(Fine)

