#from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.db import models


class Faculty(models.Model):    
    faculty_name = models.CharField( max_length=70)
           
    def __str__(self):
        return self.faculty_name

class SemesterList(models.Model):
	SEMESTER_CODE = (('i','i'), ('ii', 'ii'), ('iii','iii'), ('iv','iv'), ('v','v'), ('vi','vi'), ('vii','vii'), ('viii','viii'))
	code = models.CharField(choices=SEMESTER_CODE, max_length=4, primary_key=True)
	name = models.CharField(max_length=50)

	def __str__(self):
		return f'{self.code}'


class SubjectList(models.Model):
    code=models.CharField(max_length=70)
    name=models.CharField(max_length=255)
    target_faculty=models.ManyToManyField(Faculty, related_name='subject_list')
    target_semester=models.ManyToManyField(SemesterList, related_name='subject_list')


    def __str__(self):
        return self.name



    



