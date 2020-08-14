from django.db import models

from account.models import User
from classroom.models import Classroom


class Attendance(models.Model):
    attendance_date = models.DateField(auto_now_add=True)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_present = models.BooleanField(default=False)
