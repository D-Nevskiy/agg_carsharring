from django.core.exceptions import ValidationError
from django.core.validators import (
    MinLengthValidator,
    RegexValidator,
    MaxLengthValidator,
)


def validator_username(value):
    validator = RegexValidator(
        regex=r"^[a-zA-Z0-9]+_?[a-zA-Z0-9]+$",
        message=(
            "Неверное имя пользователя. "
            " Допускаются только буквы ангийского алфавита, цифры и знак подчеркивания."
            " Не может содержать символы «@», «.», «+» или «-»."
        ),
    )
    min_length_validator = MinLengthValidator(
        limit_value=5,
        message="Имя пользователя должно быть длиной не менее 5 символов.",
    )
    max_length_validator = MaxLengthValidator(
        limit_value=16,
        message="Имя пользователя должно быть длиной не более 16 символов.",
    )
    disallowed_value = [
        "me",
        "admin",
    ]

    if value.lower() in disallowed_value:
        raise ValidationError("Имя пользователя недопустимо.")

    validator(value)
    min_length_validator(value)
    max_length_validator(value)


def name_surname_validator(value, min_length=3):
    validator = RegexValidator(
        regex=r"^[a-zA-Zа-яА-Я]+(?:[-\s'][a-zA-Zа-яА-Я]+)*$",
        message=(
            f"Неверное значение."
            f"Допускаются только буквы, пробелы и дефисы."
        ),
    )
    min_length_validator = MinLengthValidator(
        limit_value=min_length,
        message=f"Значение поля должно быть длиной не менее {min_length} символов.",
    )

    validator(value)
    min_length_validator(value)
