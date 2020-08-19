# Generated by Django 3.1 on 2020-08-19 08:11

import assignments.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='upload',
            field=models.FileField(default='No file uploaded', upload_to=assignments.models.assignment_file_location),
        ),
        migrations.AlterField(
            model_name='submission',
            name='upload',
            field=models.FileField(upload_to=assignments.models.submission_file_location),
        ),
    ]