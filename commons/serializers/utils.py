class CurrentUserDefault:
    requires_context = True

    def __call__(self, instance):
        return instance.context["request"].user
