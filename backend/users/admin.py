from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = (
        "id",
        "username",
        "first_name",
        "last_name",
        "email",
        "mobile",
        "is_active",
    )
    search_fields = ("first_name", "last_name", "email", "mobile")
    fieldsets = (
        ("Мобильный", {"fields": ("mobile",)}),
        (
            _("Персональная информация"),
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "email",
                    "username",
                )
            },
        ),
        (
            _("Дата"),
            {
                "fields": (
                    "last_login",
                    "date_joined",
                )
            },
        ),
    )
    ordering = ("id",)
    empty_value_display = _("Пусто")
