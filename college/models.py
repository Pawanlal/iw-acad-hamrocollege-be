from django.db import models


class Faculty(models.Model):
    name = models.CharField( max_length=70)

    def __str__(self):
        return self.name


class SemesterList(models.Model):
    semester = models.CharField(max_length=30)

    def __str__(self):
        return self.semester


class SubjectList(models.Model):
    subject_code=models.CharField(max_length=30)
    name = models.CharField(max_length=255)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    semester = models.ForeignKey(SemesterList, on_delete=models.CASCADE)

    def __str__(self):
        return self.name