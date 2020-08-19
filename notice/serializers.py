from rest_framework import serializers

from .models import Category, Notice


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
