from django.db import models

from account.models import User
from classroom.models import Classroom


# Create your models here.
# Attendance - id, class_id, user_id, is_present

class Attendance(models.Model):
    attendance_date = models.DateField(auto_now_add=True, primary_key=True)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_present = models.BooleanField(default=False)
    faculty_name = models.CharField(max_length=70)


