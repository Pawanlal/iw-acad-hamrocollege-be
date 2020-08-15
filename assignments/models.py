from django.db import models
from college.models import SubjectList
from account.models import User

# Create your models here.
class Assignment(models.Model):
    title = models.CharField(max_length=255)    
    upload = models.FileField(null=True, default="No file uploaded")
    due_date = models.DateField()
    created_at = models.DateField(auto_now_add=True)
    last_updated = models.DateField(auto_now=True)    
    subject_title = models.ForeignKey(SubjectList,on_delete=models.CASCADE,
        related_name='assignments')
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='assignments'
    )

    def __str__(self):
        return self.title

class Submission(models.Model):    
    upload = models.FileField(upload_to='submissions/')
    submitted_at = models.DateField(auto_now=True)
    last_updated = models.DateField(auto_now=True)
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