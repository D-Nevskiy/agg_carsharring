from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth import get_user_model

from core.texts import (
    HELP_TEXT_CARD_NUMBER,
    HELP_TEXT_EXPIRATION_DATE,
    HELP_TEXT_CVV,
    HELP_TEXT_HOLDER_NAME,
    HELP_TEXT_USER,
    DEFAULT_LENGHT,
    MIN_LENGTH_VALIDATOR,
)

User = get_user_model()


class PaymentCard(models.Model):
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
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="payment_cards",
        help_text=HELP_TEXT_USER,
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.card_number} - {self.holder_name}"

    class Meta:
        verbose_name = "Платежная карта"
        verbose_name_plural = "Платежные карты"
