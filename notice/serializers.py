from rest_framework import serializers

from .models import Category, Notice, Comment


class CategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'category']
        read_only_fields = ['id']


class NoticeModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notice
        fields = ['id', 'text', 'file', 'category', 'date_published', 'date_updated', 'author', 'slug', 'likes']
        read_only_fields = ['id']


class CommentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'body', 'notice', 'commented_by', 'created_at', 'modified_at', 'active', 'parent']
        read_only_fields = ['id']
