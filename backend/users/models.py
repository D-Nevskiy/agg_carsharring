import uuid

from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator, validate_email
from django.db import models

from phonenumber_field.modelfields import PhoneNumberField

from bonuses.models import Bonus
from core.texts import (
    DEFAULT_LENGHT,
    HELP_TEXT_EMAIL,
    HELP_TEXT_LICENSE_IMAGE,
    HELP_TEXT_NAME,
    HELP_TEXT_PASSPORT_IMAGE,
    HELP_TEXT_PHONE_NUMBER,
    HELP_TEXT_SELFIE_IMAGE,
    HELP_TEXT_SURNAME,
    HELP_TEXT_USER_ACTIVITY,
    HELP_TEXT_VERIFICATION_STATUS,
    MIN_LENGTH_VALIDATOR,
    VERIFICATION_STATUS,
)
from core.utils import optimize_image
from orders.models import Order
from payment_cards.models import PaymentCard


class User(AbstractUser):
    # Основные персональные данные
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True,
    )
    first_name = models.CharField(
        max_length=DEFAULT_LENGHT,
        validators=[MinLengthValidator(MIN_LENGTH_VALIDATOR)],
        help_text=HELP_TEXT_NAME,
    )
    last_name = models.CharField(
        max_length=DEFAULT_LENGHT,
        validators=[MinLengthValidator(MIN_LENGTH_VALIDATOR)],
        help_text=HELP_TEXT_SURNAME,
    )

    # Контактная информация
    phone_number = PhoneNumberField(
        unique=True,
        blank=False,
        help_text=HELP_TEXT_PHONE_NUMBER,
    )
    email = models.EmailField(
        unique=True,
        validators=[validate_email],
        help_text=HELP_TEXT_EMAIL,
    )

    # Изображения
    passport_image = models.ImageField(
        upload_to="passport_images/",
        help_text=HELP_TEXT_PASSPORT_IMAGE,
    )
    driver_license_image = models.ImageField(
        upload_to="driver_license_images/",
        help_text=HELP_TEXT_LICENSE_IMAGE,
    )
    selfie_with_document = models.ImageField(
        upload_to="selfie_with_document/",
        help_text=HELP_TEXT_SELFIE_IMAGE,
    )

    # Заказы и счета
    bonuses = models.OneToOneField(
        Bonus,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    payment_cards = models.ForeignKey(
        PaymentCard,
        related_name="user_payment_cards",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    orders = models.ForeignKey(
        Order,
        related_name="user_orders",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    # Статус и активность пользователя
    status = models.CharField(
        max_length=20,
        choices=VERIFICATION_STATUS,
        default="unverified",
        help_text=HELP_TEXT_VERIFICATION_STATUS,
    )
    is_active = models.BooleanField(
        default=True,
        help_text=HELP_TEXT_USER_ACTIVITY,
    )

    def get_full_name(self):
        full_name = f"{self.first_name} {self.last_name}"
        return full_name

    def __str__(self):
        return self.get_full_name()

    def save(self, *args, **kwargs):
        """Сохранение оптимизированного изображения."""
        self.passport_image = optimize_image(self.passport_image)
        self.driver_license_image = optimize_image(self.driver_license_image)
        self.selfie_with_document = optimize_image(self.selfie_with_document)

        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        constraints = [
            models.UniqueConstraint(
                fields=("userID", "email"), name="unique_userID_email"
            )
        ]
