from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import ModelViewSet


from .models import Author, Publisher, Book, BookIssue, BookRequest, Fine
from .pagination import MyPageNumberPagination
from .permissions import IsTeacher, IsStudent, IsLibrarian
from .serializers import AuthorModelSerializer, PublisherModelSerializer, FineModelSerializer, BookModelSerializer, BookIssueModelSerializer, BookRequestModelSerializer


class AuthorModelViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorModelSerializer
    authentication_classes = [TokenAuthentication,]
    # pagination_class = MyPageNumberPagination

    def get_permissions(self):
        if self.action == 'create' or self.action == 'update' or self.action == 'destroy':
            permissions = [IsLibrarian]
        else:
            permissions = [IsAuthenticated]

        return [permission() for permission in permissions]


class PublisherModelViewSet(ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherModelSerializer
    authentication_classes = [TokenAuthentication,]
    # pagination_class = MyPageNumberPagination

    def get_permissions(self):
        if self.action == 'create' or self.action == 'update' or self.action == 'destroy':
            permissions = [IsLibrarian]
        else:
            permissions = [IsAuthenticated]

        return [permission() for permission in permissions]


class BookModelViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer
    authentication_classes = [TokenAuthentication,]
    # pagination_class = MyPageNumberPagination

    def get_permissions(self):
        if self.action == 'create' or self.action == 'update' or self.action == 'destroy':
            permissions = [IsLibrarian]
        else:
            permissions = [IsAuthenticated]

        return [permission() for permission in permissions]


class BookIssueModelViewSet(ModelViewSet):
    queryset = BookIssue.objects.all()
    serializer_class = BookIssueModelSerializer
    authentication_classes = [TokenAuthentication,]
    # pagination_class = MyPageNumberPagination

    def get_permissions(self):
        if self.action == 'create' or self.action == 'update' or self.action == 'destroy':
            permissions = [IsLibrarian]
        else:
            permissions = [IsAuthenticated]

        return [permission() for permission in permissions]


class BookRequestModelViewSet(ModelViewSet):
    queryset = BookRequest.objects.all()
    serializer_class = BookRequestModelSerializer
    authentication_classes = [TokenAuthentication, ]
    # pagination_class = MyPageNumberPagination

    def get_permissions(self):
        if self.action == 'create' or self.action == 'update' or self.action == 'destroy':
            permissions = [IsStudent | IsTeacher]
        else:
            permissions = [IsAuthenticated]

        return [permission() for permission in permissions]


class FineModelViewSet(ModelViewSet):
    queryset = Fine.objects.all()
    serializer_class = FineModelSerializer
    authentication_classes = [TokenAuthentication, ]
    # pagination_class = MyPageNumberPagination

    def get_permissions(self):
        if self.action == 'create' or self.action == 'update' or self.action == 'destroy':
            permissions = [IsLibrarian]
        else:
            permissions = [IsAuthenticated]

        return [permission() for permission in permissions]


