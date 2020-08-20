from rest_framework.authentication import TokenAuthentication

from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import ModelViewSet

from .models import Faculty, SemesterList, SubjectList, Section
from .pagination import MyPageNumberPagination
from .permissions import IsAdmin
from .serializers import FacultyModelSerializer, SemesterListModelSerializer, SubjectListModelSerializer, SectionModelSerializer


class FacultyModelViewSet(ModelViewSet):
    queryset = Faculty.objects.all()
    serializer_class = FacultyModelSerializer
    pagination_class = MyPageNumberPagination
    authentication_classes = [TokenAuthentication, ]

    def get_permissions(self):
        if self.action in ['create', 'update','partial_update', 'destroy']:
            permissions = [IsAdmin]
        else:
            permissions = [AllowAny]
        return [permission() for permission in permissions]


class SemesterListModelViewSet(ModelViewSet):
    queryset = SemesterList.objects.all()
    serializer_class = SemesterListModelSerializer
    pagination_class = MyPageNumberPagination
    authentication_classes = [TokenAuthentication, ]

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permissions = [IsAdmin]
        else:
            permissions = [AllowAny]
        return [permission() for permission in permissions]

class SectionModelViewSet(ModelViewSet):
    queryset = Section.objects.all()
    serializer_class = SectionModelSerializer
    pagination_class = MyPageNumberPagination
    authentication_classes = [TokenAuthentication, ]

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permissions = [IsAdmin]
        else:
            permissions = [AllowAny]
        return [permission() for permission in permissions]
        

class SubjectListModelViewSet(ModelViewSet):
    queryset = SubjectList.objects.all()
    serializer_class = SubjectListModelSerializer
    pagination_class = MyPageNumberPagination
    authentication_classes = [TokenAuthentication, ]

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permissions = [IsAdmin]
        else:
            permissions = [AllowAny]
        return [permission() for permission in permissions]