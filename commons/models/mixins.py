class ShowAnnotationAfterCreateMixin:
    """
    Populates created instance with manager's annotations querying it from a database.

    Important: `.create()` hits the db twice!
    """

    def create(self, **kwargs):
        instance = super().create(**kwargs)
        return self.get_queryset().get(pk=instance.pk)
