from rest_framework import serializers

from posts.models import Group, Post, Comment


class GroupSerializer(serializers.ModelSerializer):
    """
    Сериализатор модели Group.

    Model fields:
        id: int - Идентификатор группы.
        title: str - Название группы.
        slug: str - Уникальная ссылка-идентификатор группы.
        description: str - Описание группы.
    """
    class Meta:
        model = Group
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    """
    Сериализатор модели Post.

    Model fields:
        id: int - Идентификатор записи.
        author: str - Автор записи.
        pub_date: datetime - Дата публикации записи.
        group: str - Название группы, в которой опубликована запись.
        text: str - Текст записи.
        image: ImageField - Изображение, прикрепленное к записи.
    """
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        model = Post
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    """
    Сериализатор модели Comment.

    Model fields:
        id: int - Идентификатор комментария.
        author: str - Автор комментария.
        post: int - Идентификатор записи, к которой написан комментарий.
        created: datetime - Дата публикации комментария.
        text: str - Текст комментария.
    """
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('post',)
