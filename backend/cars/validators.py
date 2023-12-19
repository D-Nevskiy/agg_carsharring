from django.core.validators import RegexValidator

from core.texts import CAR_STATE_NUMBER_VALIDATOR_MESSAGE


def validate_state_number(value):
    """Валидатор для проверки корректности формата
    государственного номера автомобиля."""

    state_number_validator = RegexValidator(
        regex=r"^[а-яА-Я]{1}\d{3}[а-яА-Я]{2}\d{2,3}$",
        message=CAR_STATE_NUMBER_VALIDATOR_MESSAGE,
    )
    state_number_validator(value)
