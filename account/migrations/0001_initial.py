# Generated by Django 3.1 on 2020-08-20 14:21

import account.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=60, unique=True, verbose_name='email')),
                ('username', models.CharField(max_length=150, unique=True)),
                ('profile', models.ImageField(blank=True, null=True, upload_to=account.models.file_location)),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date_joined')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='last_login')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_teacher', models.BooleanField(default=False)),
                ('is_librarian', models.BooleanField(default=False)),
                ('is_student', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
