from django.db import models

from account.models import User
from classroom.models import Classroom
from college.models import SubjectList


class Attendance(models.Model):
    attendance_date = models.DateField(auto_now=True)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    subject = models.ForeignKey(SubjectList, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_present = models.BooleanField(default=False)

    def __str__(self):
        return self.user.first_name
