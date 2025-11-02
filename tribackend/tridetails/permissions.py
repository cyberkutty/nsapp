

from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdminOrReadCreate(BasePermission):
    """
    Allow:
      - GET, OPTIONS, HEAD => everyone (list / retrieve)
      - POST => everyone (create)
      - DELETE => only staff/superuser
      - PATCH/PUT => only staff (if you want)
    """
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS or request.method == 'POST':
            return True
        if request.method in ('DELETE','PUT','PATCH'):
            return request.user and request.user.is_authenticated and request.user.is_staff
        return False