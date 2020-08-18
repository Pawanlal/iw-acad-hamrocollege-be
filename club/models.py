import uuid

from django.db import models

from account.models import User


def file_location(instance, filename):
    extension = filename.split('.')[-1]
    unique_id = str(uuid.uuid4().hex)
    new_filename = unique_id+'.'+extension

    file_path = 'club/{new_filename}'.format(
        new_filename=new_filename
    )
    return file_path


class Club(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, unique=True)
    created_at = models.DateField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete= models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Member(models.Model):
    id = models.AutoField(primary_key=True)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_creator = models.BooleanField(default=False)

    def __str__(self):
        return self.club.name + '-' + self.user.first_name

    class Meta:
        ordering = ['club']


class Announcement(models.Model):
    id = models.AutoField(primary_key=True)
    club = models.ForeignKey(Club, on_delete= models.CASCADE)
    announce_by = models.ForeignKey(User,on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    modified_at = models.DateField(auto_now=True)
    file = models.FileField(upload_to=file_location, null=True, blank=True)

    def __str__(self):
        return self.club.name + '-' + self.message



