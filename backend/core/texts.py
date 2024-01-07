# Цифровые значения
DEFAULT_LENGHT = 100
USER_RESET_CODE_LEN = 6
MAX_RESET_ATTEMPTS = 5

# Тексты для модели Users
USER_HELP_TEXT_NAME = "Имя"
USER_HELP_TEXT_SURNAME = "Фамилия"
USER_HELP_TEXT_EMAIL = "Адрес электронной почты"
USER_RESET_CODE = "Код для сброса пароля"
USER_RESET_ATTEMPTS = "Счётчик количество попыток сброса пароля."

USER_EMAIL_VALIDATOR_MESSAGE = "Введите корректный адрес электронной почты."

USER_VERBOSE_NAME = "Пользователь"
USER_VERBOSE_NAME_PLURAL = "Пользователи"


# Тексты для модели CoordinatesCar
HELP_TEXT_LATITUDE = "Допустимый диапазон: -90.0 до 90.0"
HELP_TEXT_LONGITUDE = "Допустимый диапазон: -180.0 до 180.0"


# Тексты для модели Car
CAR_HELP_TEXT_IMAGE = "Изображение автомобиля"
CAR_IS_AVAILABLE_LABEL = "Доступна ли машина?"
CAR_COMPANY_LABEL = "Название компании каршеринга"
CAR_BRAND_LABEL = "Марка"
CAR_KIND_LABEL = "Вид"
CAR_MODEL_LABEL = "Модель"
CAR_TYPE_LABEL = "Тип"
CAR_STATE_NUMBER_LABEL = "Госномер"
CAR_STATE_NUMBER_VALIDATOR_MESSAGE = "Неверный формат госномера"
CAR_ENGINE_TYPE_LABEL = "Тип двигателя"
CAR_CHILD_SEAT_LABEL = "Присутствие детского кресла"
CAR_POWER_RESERVE_LABEL = "Запас хода"
CAR_RATING_LABEL = "Рейтинг автомобиля"
CAR_COORDINATES_LABEL = "Координаты автомобиля"
CAR_COORDINATES_HELP_TEXT = "Укажите координаты автомобиля"
CAR_VARIOUS_LABEL = "Разное"

CAR_VERBOSE_NAME = "Автомобиль"
CAR_VERBOSE_NAME_PLURAL = "Автомобили"

CAR_KIND_CAR_CHOICES = [
    ("Passenger", "Легковой"),
    ("Cargo", "Грузовой"),
]

CAR_NAME_COMPANY_CHOICES = [
    ("BelkaCar", "BelkaCar"),
    ("YandexDrive", "ЯндексДрайв"),
    ("CityDrive", "Ситидрайв"),
    ("DelyMobil", "Делимобиль"),
]
CAR_TYPE_ENGINE_CHOICES = [
    ("electro", "Электрический"),
    ("benzine", "Бензин"),
]
CAR_VARIOUS_CHOICES = [
    ("child_seat", "Детское кресло"),
    ("heated_steering_wheel", "Подогрев руля"),
    ("remote_heating", "Удаленный подогрев"),
    ("without_pasting", "Без оклейки"),
    ("shovel", "Лопата"),
    ("for_big_company", "Для большой компании"),
]
CAR_TYPE_CAR_CHOICES = [
    ("sedan", "Седан"),
    ("hatchback", "Хэтчбек"),
    ("universak", "Универсал"),
    ("kupe", "Купе"),
    ("minivan", "Минивен"),
    ("vnedorojnik", "Внедорожник"),
]
CAR_IS_AVAILABLE_CHOICES = [
    (True, "Да"),
    (False, "Нет"),
]
CAR_CHILD_SEAT_CHOICES = [
    (True, "Да"),
    (False, "Нет"),
]
