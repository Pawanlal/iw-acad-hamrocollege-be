from rest_framework import serializers

from college.models import Faculty,SemesterList,SubjectList, Section
from .models import Assignment, Submission


class AssignmentModelSerializer(serializers.ModelSerializer):
    subject_name = serializers.CharField(source='subject.name', read_only=True)
    teacher_fn = serializers.CharField(source='user.first_name', read_only=True)
    teacher_ln = serializers.CharField(source='user.last_name', read_only=True)

    class Meta:
        model = Assignment
        fields = ['id', 'title', 'upload', 'due_date', 'created_at', 'subject', 'user',
                  'subject_name', 'teacher_fn', 'teacher_ln']
        read_only_fields = ['id']


class SubmissionModelSerializer(serializers.ModelSerializer):
    user_fn = serializers.CharField(source='user.first_name', read_only=True)
    user_ln = serializers.CharField(source='user.last_name', read_only=True)
    assignment_title = serializers.CharField(source='assignment.title', read_only=True)

    class Meta:
        model = Submission
        fields = ['id', 'upload', 'submitted_at', 'assignment', 'user', 'user_fn', 'user_ln', 'assignment_title']
        read_only_fields = ['id']
