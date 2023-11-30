from django.contrib import admin

from .models import PaymentCard


@admin.register(PaymentCard)
class PaymentCardAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "card_number",
        "expiration_date",
        "cvv",
        "holder_name",
    )
    search_fields = (
        "user__first_name",
        "user__last_name",
        "user__email",
        "card_number",
    )