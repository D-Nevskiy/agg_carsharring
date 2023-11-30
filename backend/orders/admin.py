from django.contrib import admin

from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("user", "order_status", "date", "car")
    search_fields = ("user__first_name", "user__last_name", "user__email")
    list_filter = ("order_status",)


