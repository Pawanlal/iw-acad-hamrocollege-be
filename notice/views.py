from rest_framework.authentication import TokenAuthentication

from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import ModelViewSet

from .models import Category, Notice, Comment
from .pagination import MyPageNumberPagination
from .permissions import IsAdmin
from .serializers import CategoryModelSerializer, NoticeModelSerializer, CommentModelSerializer


class CategoryModelViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer
    pagination_class = MyPageNumberPagination
    authentication_classes = [TokenAuthentication, ]

    def get_permissions(self):
        if self.action in ['create', 'update', 'destroy']:
            permissions = [IsAdmin]
        else:
            permissions = [IsAuthenticated]
        return [permission() for permission in permissions]


class NoticeModelViewSet(ModelViewSet):
    queryset = Notice.objects.all()
    serializer_class = NoticeModelSerializer
    pagination_class = MyPageNumberPagination
    authentication_classes = [TokenAuthentication, ]

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permissions = [IsAdmin]
        else:
            permissions = [AllowAny]
        return [permission() for permission in permissions]


class CommentModelViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentModelSerializer
    authentication_classes = [TokenAuthentication, ]

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permissions = [IsAuthenticated]
        else:
            permissions = [AllowAny]
        return [permission() for permission in permissions]
