from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import ModelViewSet

from .models import Attendance
from .pagination import MyPageNumberPagination
from .permissions import IsTeacher
from .serializers import AttendanceModelSerializer


class AttendanceModelViewSet(ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceModelSerializer
    authentication_classes = [TokenAuthentication, ]
    pagination_class = MyPageNumberPagination

    def get_permissions(self):
        if self.action == 'create' or self.action == 'update':
            permissions = [IsTeacher]

        else:
            permissions = [IsAuthenticated]

        return [permission() for permission in permissions]

