from django.db import models

import datetime

class Classroom(models.Model):

    classroom_id = models.AutoField(primary_key=True)
    classroom_title = models.CharField(max_length=100)
    classroom_created_at = models.DateTimeField(auto_now_add=True)
    classroom_creator = models.CharField(max_length=100)
    classroom_faculty = models.CharField(max_length=100)


    def __str__(self):
        return self.classroom_title


class ClassroomMember(models.Model):
    member_id = models.AutoField(primary_key=True)
    classroom_id = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    # classroom_id = models.IntegerField()
    user_id = models.IntegerField()
    # is_creator = models.BooleanField(default=False)
    # user_id = models.ForeignKey(User, on_delete= models.CASCADE)
    # is_creator = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.is_creator


class ClassDiscussion(models.Model):
    discussion_id = models.AutoField(primary_key=True)
    classroom_id = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    # user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    # classroom_id = models.IntegerField()
    user_id = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    comment = models.TextField()
    # file = models.FileField()

    def __str__(self):
        return self.comment

