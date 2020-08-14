from django.db import models
from account.models import User

import datetime

class Classroom(models.Model):

    classroom_id = models.AutoField(primary_key=True)
    classroom_title = models.CharField(max_length=100, unique=True)
    classroom_created_at = models.DateTimeField(auto_now_add=True)
    classroom_creator = models.CharField(max_length=100)
    classroom_faculty = models.CharField(max_length=100)


    def __str__(self):
        return self.classroom_title


class ClassroomMember(models.Model):
    member_id = models.AutoField(primary_key=True)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_creator = models.BooleanField(default=False)

    def __str__(self):
        return self.is_creator


class ClassroomDiscussion(models.Model):
    discussion_id = models.AutoField(primary_key=True)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    comment = models.TextField()
    # file = models.FileField()

    def __str__(self):
        return self.comment

