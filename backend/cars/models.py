from django.db import models


class Car(models.Model):
    """Тестовая модель."""

    brand = models.CharField(
        max_length=255,
        verbose_name='Марка',
    )
    model = models.CharField(
        max_length=255,
        verbose_name='Модель',
    )


