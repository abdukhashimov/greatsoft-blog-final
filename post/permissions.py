from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsAuthorOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user


class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user.is_superuser


class IsPostCorrect(BasePermission):
    def has_object_permission(self, request, view, obj):
        cust_id = request.data.get('parent')
        if not cust_id:
            return True
        for comment in obj.get_comments:
            if str(comment.id) == str(cust_id):
                return True
            for child_comment in comment.child_comments:
                if str(child_comment.id) == str(cust_id):
                    return True
        return False
