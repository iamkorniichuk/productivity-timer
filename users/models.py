from django.db import models
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin,
)
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    def create_user(self, email, password, **kwargs):
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **kwargs):
        user = self.create_user(email=email, password=password, **kwargs)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class User(PermissionsMixin, AbstractBaseUser):
    email = models.EmailField(_("email"), unique=True)
    password = models.CharField(_("password"), max_length=88)

    is_active = models.BooleanField(_("is active"), default=True)
    is_staff = models.BooleanField(_("is staff"), default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["password"]

    objects = UserManager()

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"pk": self.pk})

    def __str__(self):
        return str(self.email)
