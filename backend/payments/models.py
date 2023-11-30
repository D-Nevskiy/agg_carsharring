
from django.core.validators import MinLengthValidator
from django.db import models
from django.conf import settings

from core.texts import (
    HELP_TEXT_USER,
    MIN_LENGTH_VALIDATOR,
    HELP_TEXT_CARD_NUMBER,
    HELP_TEXT_EXPIRATION_DATE,
    HELP_TEXT_CVV,
    HELP_TEXT_HOLDER_NAME,
    DEFAULT_LENGHT,
)


class PaymentCard(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="user_payment_cards",
        help_text=HELP_TEXT_USER,
    )
    card_number = models.CharField(
        max_length=16,
        validators=[MinLengthValidator(MIN_LENGTH_VALIDATOR)],
        help_text=HELP_TEXT_CARD_NUMBER,
    )
    expiration_date = models.DateField(
        help_text=HELP_TEXT_EXPIRATION_DATE,
    )
    cvv = models.CharField(
        max_length=3,
        validators=[MinLengthValidator(MIN_LENGTH_VALIDATOR)],
        help_text=HELP_TEXT_CVV,
    )
    holder_name = models.CharField(
        max_length=DEFAULT_LENGHT,
        help_text=HELP_TEXT_HOLDER_NAME,
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.card_number} - {self.holder_name}"

    class Meta:
        verbose_name = "Платежная карта"
        verbose_name_plural = "Платежные карты"
