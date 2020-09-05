import uuid

from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver

from college.models import SubjectList
from account.models import User


def submission_file_location(instance, filename):
    extension = filename.split('.')[-1]
    unique_id = str(uuid.uuid4())
    new_filename = unique_id+'.'+extension
    file_path = 'submission/{new_filename}'.format(
        new_filename=new_filename
    )
    return file_path


def assignment_file_location(instance, filename):
    extension = filename.split('.')[-1]
    unique_id = str(uuid.uuid4())
    new_filename = unique_id+'.'+extension
    file_path = 'assignment/{new_filename}'.format(
        new_filename=new_filename
    )
    return file_path


class Assignment(models.Model):
    title = models.CharField(max_length=255)    
    upload = models.FileField(upload_to=assignment_file_location, null=False, default="No file uploaded", blank=False)
    due_date = models.DateField()
    created_at = models.DateField(auto_now_add=True)    
    subject = models.ForeignKey(SubjectList,on_delete=models.CASCADE, related_name='assignments')
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='assignments'
    )

    def __str__(self):
        return self.title


class Submission(models.Model):
    upload = models.FileField(upload_to=submission_file_location, null=False, blank=False)
    submitted_at = models.DateField(auto_now=True)    
    assignment = models.ForeignKey(
        'Assignment',
        on_delete=models.CASCADE,
        related_name='submissions'
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='submissions'
    )

    def __str__(self):
        return self.user.first_name


@receiver(post_delete, sender=Assignment)
def assignment_delete(sender, instance, **kwargs):
    instance.upload.delete(False)


@receiver(post_delete, sender=Submission)
def submission_delete(sender, instance, **kwargs):
    instance.upload.delete(False)
