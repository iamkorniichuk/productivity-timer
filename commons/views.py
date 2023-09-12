class UserRelatedObjectsMixin:
    """
    Limits queryset to objects which include FK to current logged in user.

    Override `user_field_name` to specify user field's name in serializer.
    """

    user_field_name = "user"

    def get_queryset(self):
        return super().get_queryset().filter(**self.user_kwargs)

    def perform_create(self, serializer):
        serializer.save(**self.user_kwargs)

    @property
    def user_kwargs(self):
        return {self.user_field_name: self.request.user}
