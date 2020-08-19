import uuid

from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save, post_delete
from django.dispatch import receiver
from django.utils.text import slugify


def file_location(instance, filename):
    extension = filename.split('.')[-1]
    author_id = str(instance.author.id)
    unique_id = str(uuid.uuid4())
    new_filename = unique_id+'.'+extension

    file_path = 'collegenotice/{author_id}/{new_filename}'.format(
        author_id=author_id,
        new_filename=new_filename
    )
    return file_path


class Category(models.Model):
    category = models.CharField(max_length=30)

    def __str__(self):
        return self.category


class Notice(models.Model):
    text = models.TextField(max_length=5000)
    file = models.FileField(upload_to=file_location, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date_published = models.DateTimeField(auto_now_add=True, verbose_name="date published")
    date_updated = models.DateTimeField(auto_now=True, verbose_name="date updated")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    slug = models.SlugField(blank=True, unique=True)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='notice_like')

    def __str__(self):
        return self.slug


class Comment(models.Model):
    notice = models.ForeignKey(Notice, on_delete=models.CASCADE)
    body = models.CharField(max_length=500)
    commented_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='notice_comment')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    # manually deactivate inappropriate comments by admin
    active = models.BooleanField(default=True)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='replies', on_delete=models.CASCADE)


@receiver(post_delete, sender=Notice)
def submission_delete(sender, instance, **kwargs):
    instance.file.delete(False)


def pre_save_notice_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(uuid.uuid4())


pre_save.connect(pre_save_notice_receiver, sender=Notice)
