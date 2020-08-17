# Generated by Django 3.1 on 2020-08-17 12:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='SemesterList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='SubjectList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_code', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=255)),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='college.faculty')),
                ('semester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='college.semesterlist')),
            ],
        ),
    ]
