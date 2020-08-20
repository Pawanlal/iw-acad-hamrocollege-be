from rest_framework import serializers

from .models import Classroom, ClassroomMember, ClassroomDiscussion, Comment


class ClassroomModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = ['id', 'title', 'created_at', 'updated_at', 'passcode', 'creator_id', 'faculty', 'section']
        read_only_fields = ['id']


class ClassroomDiscussionModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassroomDiscussion
        fields = ['id', 'created_at', 'modified_at', 'text', 'file', 'classroom', 'user']
        read_only_fields = ['id']


class ClassroomMemberModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassroomMember
        fields = ['id', 'is_creator', 'classroom', 'user']
        read_only_fields = ['id']


class CommentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'body', 'created_at', 'modified_at', 'active', 'classroom_discussion', 'commented_by', 'parent']
        read_only_fields = ['id']
