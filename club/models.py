from django.db import models

from account.models import User

# Create your models here.

class Club(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, unique=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.first_name

    class Meta:
        ordering = ['name']


class Member(models.Model):
    id = models.AutoField(primary_key = True)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_creator = models.BooleanField(default=False)

    def __str__(self):
        return self.club.name + '-' + self.user.name

    class Meta:
        ordering = ['club']


class Announcement(models.Model):
    id = models.AutoField(primary_key=True)
    club = models.ForeignKey(Club, on_delete= models.CASCADE)
    announce_by = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    modified_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.club.name + '-' + self.message


