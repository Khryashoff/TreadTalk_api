from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied


class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Проверка разрешений для объекта.

    Аутентифицированным пользователям доступно только чтение.
    Аутентифицированные авторы публикаций могут редактировать или удалять их.
    """
    def has_object_permission(self, request, view, obj):
        """
        Проверяет, имеет ли пользователь право на данное действие над объектом.
        """
        if (request.method in permissions.SAFE_METHODS
                or obj.author == request.user):
            return True
        raise PermissionDenied('Вы не являетесь автором этой записи. '
                               'Редактирование не доступно.')
