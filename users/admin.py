from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ["pk", "email", "is_staff"]
    ordering = ["email"]
    add_fieldsets = [
        (None, {"fields": ["email", "password1", "password2", "is_staff"]}),
    ]
    fieldsets = [
        (None, {"fields": ["email", "password", "is_staff"]}),
    ]
