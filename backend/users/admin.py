from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from .models import Bonus, User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = (
        "id",
        "mobile",
        "first_name",
        "last_name",
        "email",
        "status",
        "is_active",
    )
    search_fields = ("first_name", "last_name", "email", "mobile")
    list_filter = ("status", "is_active")

    fieldsets = (
        (None, {"fields": ("mobile",)}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email")}),
        (
            _("Image"),
            {
                "fields": (
                    "passport_image",
                    "driver_license_image",
                    "selfie_with_document",
                )
            },
        ),
        (
            _("Orders and cards"),
            {
                "fields": (
                    "bonuses",
                    "payment_cards",
                    "orders",
                )
            },
        ),
        (_("Date"), {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("mobile", "password1", "password2"),
            },
        ),
    )


@admin.register(Bonus)
class BonusAdmin(admin.ModelAdmin):
    list_display = ("user", "amount", "created_at", "updated_at")
    search_fields = ("user__first_name", "user__last_name", "user__email")
