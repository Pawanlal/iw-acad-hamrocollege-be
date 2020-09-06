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
    author_fn = serializers.CharField(source='author.firstname', read_only=True)
    author_ln = serializers.CharField(source='author.lastname', read_only=True)
    publisher_name = serializers.CharField(source='publisher.name', read_only=True)

    class Meta:
        model = Book
        fields = ['id', 'title', 'isbn', 'publisher', 'edition', 'author', 'author_fn', 'author_ln', 'publisher_name']
        read_only_fields = ['id']


class BookIssueModelSerializer(serializers.ModelSerializer):
    book_name = serializers.CharField(source='book.title', read_only=True)
    user_fn = serializers.CharField(source='user.first_name', read_only=True)
    user_ln = serializers.CharField(source='user.last_name', read_only=True)

    class Meta:
        model = BookIssue
        fields = ['id', 'user', 'book', 'issue_date', 'return_date', 'book_name', 'user_fn', 'user_ln']
        read_only_fields = ['id']


class BookRequestModelSerializer(serializers.ModelSerializer):
    book_name = serializers.CharField(source='book.title', read_only=True)
    user_fn = serializers.CharField(source='user.first_name', read_only=True)
    user_ln = serializers.CharField(source='user.last_name', read_only=True)

    class Meta:
        model = BookRequest
        fields = ['id', 'user', 'book', 'status', 'request_date', 'book_name', 'user_fn', 'user_ln']
        read_only_fields = ['id']


class FineModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fine
        fields = '__all__'
        read_only_fields = ['id']

