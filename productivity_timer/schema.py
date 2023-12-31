from django.utils.translation import gettext_lazy as _
from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title=_("Productivity Timer"),
        default_version="v0.0.8",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
    authentication_classes=[],
)
