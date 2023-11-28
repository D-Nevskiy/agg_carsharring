import uuid

from django.utils import timezone

from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.core.validators import MinLengthValidator, validate_email
from django.db import models

from phonenumber_field.modelfields import PhoneNumberField

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
    HELP_TEXT_ORDER_STATUS,
    HELP_TEXT_CARD_NUMBER,
    HELP_TEXT_EXPIRATION_DATE,
    HELP_TEXT_CVV,
    HELP_TEXT_HOLDER_NAME,
    HELP_TEXT_USER,
    MIN_LENGTH_VALIDATOR,
    VERIFICATION_STATUS,
    ORDER_STATUS,
)
from core.utils import optimize_image


class UserCustomManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, phone_number, password, **extra_fields):
        if not phone_number:
            raise ValueError("The given phonenumber must be set")
        user = self.model(
            phone_number=phone_number, username=phone_number, **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, phone_number, password, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(phone_number, password, **extra_fields)

    def create_superuser(self, phone_number, password, **extra_fields):
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
        "PaymentCard",
        related_name="payment_cards",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    orders = models.ForeignKey(
        "Order",
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
        User,
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


class Order(models.Model):
    user = models.ForeignKey(
        User,
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
    car = models.ForeignKey("Car", on_delete=models.CASCADE)
    # Начало координат
    start_latitude = models.DecimalField(max_digits=9, decimal_places=6)
    start_longitude = models.DecimalField(max_digits=9, decimal_places=6)
    # Конец координат
    end_latitude = models.DecimalField(max_digits=9, decimal_places=6)
    end_longitude = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return f"Order for {self.user.id}, State: {self.order_status}, Date: {self.date}, Car: {self.car}"


class Car(models.Model):
    """Тестовая модель."""

    brand = models.CharField(max_length=255)
    model = models.CharField(max_length=255)


class PaymentCard(models.Model):
    user = models.ForeignKey(
        User,
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
