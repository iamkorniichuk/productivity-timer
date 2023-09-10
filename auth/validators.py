from django.contrib.auth.password_validation import validate_password


class PasswordValidator:
    def __init__(self, user=None):
        self.user = user

    def __call__(self, value):
        validate_password(value, self.user)
