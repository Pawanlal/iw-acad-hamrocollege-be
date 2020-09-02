from rest_framework.permissions import BasePermission


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_admin


class IsCreator(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.member.is_creator
