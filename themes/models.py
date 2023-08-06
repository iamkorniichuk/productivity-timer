from django.db import models
from django.utils.translation import gettext_lazy as _


class Theme(models.Model):
    name = models.CharField(_("name"), max_length=64)
    parent = models.ForeignKey(
        "themes.Theme",
        models.CASCADE,
        null=True,
        blank=True,
        related_name="children",
        verbose_name=_("parent"),
    )

    def __str__(self):
        return self.name
