from rest_framework.permissions import BasePermission

class IsAdminOrSuperUser(BasePermission):
    def has_permission(self, request, view):
        # Only allow editing if the user is an admin or superuser
        if request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            return request.user and request.user.is_staff  # or request.user.is_superuser for more restriction
        return True 