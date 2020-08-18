import math
import random
import uuid

from django.conf import settings
from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver

from account.models import User
from college.models import Section, Faculty, SubjectList


def file_location(instance, filename):
    extension = filename.split('.')[-1]
    unique_id = str(uuid.uuid4().hex)
    new_filename = unique_id+'.'+extension

    file_path = 'classroom/{new_filename}'.format(
        new_filename=new_filename
    )
    return file_path


def access_code():
    string = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    length = len(string)
    code = ""
    for i in range(8):
        code += string[math.floor(random.random() * length)]
    return code


class Classroom(models.Model):
    title = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    section = models.OneToOneField(Section, on_delete=models.CASCADE)
    subject = models.ManyToManyField(SubjectList)
    passcode = models.CharField(max_length=8, default=access_code)

    def __str__(self):
        return self.title


class ClassroomMember(models.Model):
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_creator = models.BooleanField(default=False)

    def __str__(self):
        return self.user.first_name


class ClassroomDiscussion(models.Model):
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    text = models.TextField(max_length=5000)
    file = models.FileField(upload_to=file_location)

    def __str__(self):
        return self.user.first_name


class Comment(models.Model):
    classroom_discussion = models.ForeignKey(ClassroomDiscussion, on_delete=models.CASCADE)
    body = models.CharField(max_length=500)
    commented_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    # manually deactivate inappropriate comments by admin
    active = models.BooleanField(default=True)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='replies', on_delete=models.CASCADE)


@receiver(post_delete, sender=ClassroomDiscussion)
def submission_delete(sender, instance, **kwargs):
    instance.file.delete(False)
