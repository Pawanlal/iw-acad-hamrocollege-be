from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet


from .models import Classroom, ClassroomDiscussion, ClassroomMember, Comment
from .pagination import MyPageNumberPagination
from .permissions import IsTeacher, IsStudent
from .serializers import ClassroomModelSerializer, ClassroomDiscussionModelSerializer, ClassroomMemberModelSerializer, CommentModelSerializer

class ClassroomModelViewSet(ModelViewSet):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomModelSerializer
    authentication_classes = [TokenAuthentication,]
    pagination_class = MyPageNumberPagination

    def get_permissions(self):
        if self.action == 'create' or self.action == 'update' or self.action == 'destroy':
            permissions = [IsTeacher]
        else:
            permissions = [IsAuthenticated]

        return [permission() for permission in permissions]


class ClassroomDiscussionModelViewSet(ModelViewSet):
    queryset = ClassroomDiscussion.objects.all()
    serializer_class = ClassroomDiscussionModelSerializer
    authentication_classes = [TokenAuthentication,]
    pagination_class = MyPageNumberPagination

    def get_permissions(self):
        if self.action == 'create' or self.action == 'update' or self.action == 'destroy':
            permissions = [IsTeacher, IsStudent]

        else:
            permissions = [IsAuthenticated]

        return [permission() for permission in permissions]

class ClassroomMemberModelViewSet(ModelViewSet):
    queryset = ClassroomMember.objects.all()
    serializer_class = ClassroomMemberModelSerializer
    authentication_classes = [TokenAuthentication,]
    pagination_class = MyPageNumberPagination

    def get_permissions(self):
        if self.action == 'create' or self.action == 'update' or self.action == 'destroy':
            permissions = [IsTeacher]

        else:
            permissions = [IsAuthenticated]

        return [permission() for permission in permissions]


class CommentModelViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentModelSerializer
    authentication_classes = [TokenAuthentication,]

    def get_permissions(self):
        if self.action == 'create' or self.action == 'update' or self.action == 'destroy':
            permissions = [IsTeacher,IsStudent]

        else:
            permissions = [IsAuthenticated]

        return [permission() for permission in permissions]




