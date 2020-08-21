from rest_framework import serializers

from college.models import Faculty,SemesterList,SubjectList, Section
from .models import Assignment, Submission


class AssignmentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields =  '__all__'
        read_only_fields = ['id']


class SubmissionModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields =  '__all__'
        read_only_fields = ['id']
        