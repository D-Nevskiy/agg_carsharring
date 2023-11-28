from django.db import models

from users.models import User
from core.texts import ORDER_STATUS, HELP_TEXT_ORDER_STATUS


class Order(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="oreders",
    )
    order_status = models.CharField(
        choices=ORDER_STATUS,
        default="Finished",
        help_text=HELP_TEXT_ORDER_STATUS,
    )
    date = models.DateField()
    car = models.ForeignKey("Car", on_delete=models.CASCADE)
    # Начало координат
    start_latitude = models.DecimalField(max_digits=9, decimal_places=6)
    start_longitude = models.DecimalField(max_digits=9, decimal_places=6)
    # Конец координат
    end_latitude = models.DecimalField(max_digits=9, decimal_places=6)
    end_longitude = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return f"Order for {self.user.id}, State: {self.state}, Date: {self.date}, Car: {self.car}"


class Car(models.Model):
    """Тестовая модель."""
    brand = models.CharField(max_length=255)
    model = models.CharField(max_length=255)