from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from posts.models import Group, Post

from api.permissions import IsAuthorOrReadOnly
from api.serializers import (GroupSerializer, PostSerializer,
                             CommentSerializer)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Набор представлений для работы с группами.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated]


class PostViewSet(viewsets.ModelViewSet):
    """
    Набор представлений для работы с постами.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        """
        Создает новый пост и сохраняет информацию об авторе поста.
        """
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    """
    Набор представлений для обработки комментариев, связанных с постом.
    """
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    def get_queryset(self):
        """
        Возвращает queryset, который содержит все комментарии,
        связанные с определенным постом.
        """
        post = get_object_or_404(Post, id=self.kwargs.get('post_id'))
        return post.comments.all()

    def perform_create(self, serializer):
        """
        Создает новый комментарий, связанный с определенным постом.
        """
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        serializer.save(author=self.request.user, post=post)
