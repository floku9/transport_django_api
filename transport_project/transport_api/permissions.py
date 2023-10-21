from rest_framework import permissions


class IsInSameCompany(permissions.BasePermission):
    """
    Custom permission to only allow users to view objects from their own company.
    """

    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        if request.user.company:
            # Assuming you have a company field in the user model
            company_id = request.user.company.id
            if view.kwargs.get('company_id'):
                return int(view.kwargs.get('company_id')) == company_id
            elif 'company_id' in request.data:
                return int(request.data['company_id']) == company_id
            return True
        return False
