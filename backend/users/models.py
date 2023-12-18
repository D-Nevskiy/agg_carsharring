from django.contrib.auth.models import AbstractUser
from django.core.validators import EmailValidator
from django.db import models

from phonenumber_field.modelfields import PhoneNumberField

from core.texts import (
    DEFAULT_LENGHT,
    USER_EMAIL_VALIDATOR_MESSAGE,
    USER_HELP_TEXT_EMAIL,
    USER_HELP_TEXT_NAME,
    USER_HELP_TEXT_PHONE_NUMBER,
    USER_HELP_TEXT_SURNAME,
    USER_HELP_TEXT_USERNAME,
    USER_VERBOSE_NAME,
    USER_VERBOSE_NAME_PLURAL,
    USER_USERNAME_ERROR_MESSAGE,
)
from .validators import name_surname_validator, validator_username


class User(AbstractUser):
    """
    Расширенная модель пользователя с дополнительными полями.
    """

    email = models.EmailField(
        max_length=DEFAULT_LENGHT,
        unique=True,
        validators=[
            EmailValidator(message=USER_EMAIL_VALIDATOR_MESSAGE),
        ],
        help_text=USER_HELP_TEXT_EMAIL,
    )

    username = models.CharField(
        max_length=DEFAULT_LENGHT,
        unique=True,
        db_index=True,
        validators=[
            validator_username,
        ],
        error_messages={
            "unique": USER_USERNAME_ERROR_MESSAGE,
        },
        help_text=USER_HELP_TEXT_USERNAME,
    )

    first_name = models.CharField(
        max_length=DEFAULT_LENGHT,
        validators=[
            name_surname_validator,
        ],
        help_text=USER_HELP_TEXT_NAME,
    )

    last_name = models.CharField(
        max_length=DEFAULT_LENGHT,
        validators=[
            name_surname_validator,
        ],
        help_text=USER_HELP_TEXT_SURNAME,
    )
    mobile = PhoneNumberField(
        unique=True,
        blank=True,
        null=True,
        help_text=USER_HELP_TEXT_PHONE_NUMBER,
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [
        "username",
        "first_name",
        "last_name",
    ]

    class Meta:
        verbose_name = USER_VERBOSE_NAME
        verbose_name_plural = USER_VERBOSE_NAME_PLURAL
        constraints = [
            models.UniqueConstraint(
                fields=("username", "email"),
                name="unique_username_email",
            )
        ]

    def __str__(self) -> str:
        return self.username
