from rest_framework import serializers

from .models import Faculty,SemesterList,SubjectList, Section


class FacultyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = ['id', 'name']
        read_only_fields = ['id']


class SemesterListModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = SemesterList
        fields = ['id', 'semester']
        read_only_fields = ['id']

class SectionModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = ['id', 'section']
        read_only_fields = ['id']


class SubjectListModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubjectList
        fields = ['id', 'subject_code', 'name', 'faculty', 'semester']
        read_only_fields = ['id']

