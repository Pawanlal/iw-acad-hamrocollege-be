import uuid

from django.db import models
from account.models import User


def file_location(instance, filename):
    extension = filename.split('.')[-1]
    unique_id = str(uuid.uuid4().hex)
    new_filename = unique_id+'.'+extension

    file_path = 'classroom/{new_filename}'.format(
        new_filename=new_filename
    )
    return file_path


class Classroom(models.Model):
    title = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    faculty = models.CharField(max_length=100)
    passcode = models.CharField(max_length=8)

    def __str__(self):
        return self.title


class ClassroomMember(models.Model):
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_creator = models.BooleanField(default=False)


class ClassroomDiscussion(models.Model):
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    text = models.TextField(max_length=5000)
    file = models.FileField(upload_to=file_location)

    def __str__(self):
        return self.comment

