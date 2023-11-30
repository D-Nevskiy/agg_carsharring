import uuid
from django.utils import timezone
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.core.validators import MinLengthValidator, validate_email
from django.conf import settings
from django.db import models

from phonenumber_field.modelfields import PhoneNumberField

from orders.models import Order
from payments.models import PaymentCard
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


class UserCustomManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, phone_number, password=None, **extra_fields):
        if not phone_number:
            raise ValueError("The given phonenumber must be set")
        user = self.model(
            phone_number=phone_number, username=phone_number, **extra_fields
        )
        if password is not None:
            user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, phone_number, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(phone_number, password, **extra_fields)

    def create_superuser(self, phone_number, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(phone_number, password, **extra_fields)


class User(AbstractUser):
    # Основные персональные данные
    userID = models.UUIDField(
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
        "Bonus",
        related_name="bonuses",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    payment_cards = models.ForeignKey(
        PaymentCard,
        related_name="payment_cards",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    orders = models.ForeignKey(
        Order,
        related_name="orders",
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

    objects = UserCustomManager()

    USERNAME_FIELD = "phone_number"

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


class Bonus(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="user_bonuses",
    )
    amount = models.IntegerField(default=0)
    created_at = models.DateTimeField(
        default=timezone.now,
        editable=False,
    )
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.email}'s Bonuses"
