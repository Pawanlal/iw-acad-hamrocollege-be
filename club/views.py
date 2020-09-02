from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import ModelViewSet

from .models import Club, Member, Announcement
from .pagination import MyPageNumberPagination
from .permissions import IsAdmin, IsCreator

from .serializers import AnnouncementModelSerializer, ClubModelSerializer, MemberModelSerializer


class AnnouncementModelViewSet(ModelViewSet):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementModelSerializer
    pagination_class = MyPageNumberPagination
    authentication_classes = [TokenAuthentication, ]

    def get_permissions(self):
        if self.action == 'create' or self.action == 'update' or self.action == 'destroy':
            permissions = [IsAdmin, IsCreator]

        else:
            permissions = [AllowAny]

        return [permission() for permission in permissions]


class ClubModelViewSet(ModelViewSet):
    queryset = Club.objects.all()
    serializer_class = ClubModelSerializer
    pagination_class = MyPageNumberPagination
    authentication_classes = [TokenAuthentication, ]

    def get_permissions(self):
        if self.action == 'create' or self.action == 'update' or self.action == 'destroy':
            permissions = [IsAdmin, IsCreator]

        else:
            permissions = [AllowAny]

        return [permission() for permission in permissions]


class MemberModelViewSet(ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberModelSerializer
    pagination_class = MyPageNumberPagination
    authentication_classes = [TokenAuthentication, ]

    def get_permissions(self):
        if self.action == 'create' or self.action == 'update' or self.action == 'destroy':
            permissions = [IsAdmin, IsCreator]

        else:
            permissions = [IsAuthenticated]

        return [permission() for permission in permissions]



