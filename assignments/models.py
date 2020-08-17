from django.db import models
from college.models import SubjectList
from account.models import User

# Create your models here.
class Assignment(models.Model):
    title = models.CharField(max_length=255)    
    upload = models.FileField(upload_to='assign/',null=False, default="No file uploaded", blank=False)
    due_date = models.DateField()
    created_at = models.DateField(auto_now_add=True)    
    subject = models.ForeignKey(SubjectList,on_delete=models.CASCADE,
        related_name='assignments')
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='assignments'
    )

    def __str__(self):
        return self.title

class Submission(models.Model):    
    upload = models.FileField(upload_to='submissions/',null=False, blank=False)
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