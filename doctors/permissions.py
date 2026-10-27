from rest_framework import permissions


class IsCreatorOrReadOnly(permissions.BasePermission):
    """Any authenticated user may read; only the creator may edit/delete."""

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.created_by == request.user
