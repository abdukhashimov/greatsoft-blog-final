from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsUserCorrect(BasePermission):
    def has_object_permission(self, request, view, obj):
        return False
