from django.db import models
from django.conf import settings

from core.texts import (
    DEFAULT_LENGHT,
    ORDER_STATUS,
    HELP_TEXT_ORDER_STATUS,
)

from cars.models import Car


class Order(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="user_orders",
    )
    order_status = models.CharField(
        max_length=DEFAULT_LENGHT,
        choices=ORDER_STATUS,
        default="Finished",
        help_text=HELP_TEXT_ORDER_STATUS,
    )
    date = models.DateField()
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    # Начало координат
    start_latitude = models.DecimalField(max_digits=9, decimal_places=6)
    start_longitude = models.DecimalField(max_digits=9, decimal_places=6)
    # Конец координат
    end_latitude = models.DecimalField(max_digits=9, decimal_places=6)
    end_longitude = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return f"Order for {self.user.id}, State: {self.order_status}, Date: {self.date}, Car: {self.car}"
