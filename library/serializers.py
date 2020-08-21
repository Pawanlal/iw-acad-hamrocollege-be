from rest_framework import serializers

from college.models import Faculty,SemesterList,SubjectList, Section
from .models import Author, Publisher, Book, BookIssue, BookRequest, Fine



class AuthorModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'
        read_only_fields = ['id']


class PublisherModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = '__all__'
        read_only_fields = ['id']

class BookModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        read_only_fields = ['id']


class BookIssueModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookIssue
        fields = '__all__'
        read_only_fields = ['id']


class BookRequestModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookRequest
        fields = '__all__'
        read_only_fields = ['id']


class FineModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fine
        fields = '__all__'
        read_only_fields = ['id']

