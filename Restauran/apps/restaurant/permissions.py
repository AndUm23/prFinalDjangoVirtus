from rest_framework import permissions

class IsManagerOrAdminTables(permissions.BasePermission):
    def has_permission(self, request, view):
        # Check if the user has the necessary role (Manager or AdminTables)
        return request.user.waiter.charge in ['MG', 'AT']

class IsManager(permissions.BasePermission):
    def has_permission(self, request, view):
        # Check if the user has the necessary role (Manager)
        return request.user.waiter.charge == 'MG'
