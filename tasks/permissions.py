from rest_framework import permissions

class IsAdminOrAssignedUser(permissions.BasePermission):
    """
    Custom permission to only allow admins or the user assigned to the task to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Write permissions are only allowed to the admin or the assigned user.
        return request.user.is_staff or obj.assigned_to == request.user
