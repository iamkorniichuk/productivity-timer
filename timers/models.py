from django.db import models
from django.utils.translation import gettext_lazy as _


class Timer(models.Model):
    start = models.DateTimeField(_("start"), auto_now_add=True)
    end = models.DateTimeField(_("end"), null=True, blank=True)
    set_date = models.DateField(_("set date"), null=True, blank=True)

    def __str__(self):
        return str(self.start)
