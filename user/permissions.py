from rest_framework import permissions


class IsOwnerOrAdmin(permissions.BasePermission):

    message = "You don't own this collection. Access denied."

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
