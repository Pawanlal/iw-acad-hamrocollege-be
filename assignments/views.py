from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import ModelViewSet


from .models import Assignment, Submission
from .pagination import MyPageNumberPagination
from .permissions import IsTeacher, IsStudent
from .serializers import AssignmentModelSerializer, SubmissionModelSerializer


class AssignmentModelViewSet(ModelViewSet):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentModelSerializer
    authentication_classes = [TokenAuthentication,]
    pagination_class = MyPageNumberPagination

    def get_permissions(self):
        if self.action == 'create' or self.action == 'update' or self.action == 'destroy':
            permissions = [IsTeacher]
        else:
            permissions = [IsAuthenticated]

        return [permission() for permission in permissions]


class SubmissionModelViewSet(ModelViewSet):
    queryset=Submission.objects.all()
    serializer_class=SubmissionModelSerializer
    authentication_classes=[TokenAuthentication,]
    pagination_class=MyPageNumberPagination

    def get_permissions(self):
        if self.action == 'create' or self.action == 'destroy':
            permissions = [IsTeacher]
        else:
            permissions = [IsAuthenticated]

        return [permission() for permission in permissions]