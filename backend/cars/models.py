from django.db import models
from django.core.validators import RegexValidator


class CoordinatesCar(models.Model):
    latitude = models.FloatField(
        'Широта',
        max_length=8
    )
    longitude = models.FloatField(
        'Долгота',
        max_length=8
    )

    class Meta:
        verbose_name = 'Координата'
        verbose_name_plural = 'Координаты'

    def __str__(self):
        return f'[{self.latitude}]: {self.longitude}'


class Car(models.Model):
    NAME_COMPANY_CHOICES = [
        ('BelkaCar', 'BelkaCar'),
        ('YandexDrive', 'ЯндексДрайв'),
        ('CityDrive', 'Ситидрайв'),
    ]
    TYPE_ENGINE_CHOICES = [
        ('electro', 'Электрический'),
        ('benzine', 'Бензин'),
    ]
    TYPE_CAR_CHOICES = [
        ('sedan', 'Седан'),
        ('hatchback', 'Хэтчбек'),
        ('minivan', 'Минивен'),
    ]

    image = models.ImageField(
        upload_to='cars/images/',
        null=True,
        default=None
    )
    is_available = models.BooleanField(
        'Доступна ли машина?',
        default=True
    )
    company = models.CharField(
        'Название компании каршеринга',
        choices=NAME_COMPANY_CHOICES,
        max_length=30
    )
    brand = models.CharField(
        'Марка',
        max_length=30
    )
    model = models.CharField(
        'Модель',
        max_length=30
    )
    type_car = models.CharField(
        'Тип',
        choices=TYPE_CAR_CHOICES,
        max_length=30
    )
    state_number = models.CharField(
        'Госномер',
        max_length=10,
        validators=[
            RegexValidator(
                regex=r'^[а-яА-Я]{1}\d{3}[а-яА-Я]{2}\d{3}$|^[а-яА-Я]{1}\d{3}[а-яА-Я]{2}\d{2}$',
                message='Неверый формат госномера'
            )
        ]
    )
    type_engine = models.CharField(
        'Тип двигателя',
        choices=TYPE_ENGINE_CHOICES,
        max_length=30
    )
    child_seat = models.BooleanField(
        'Присутствие десткого кресла',
        default=False
    )
    power_reserve = models.IntegerField(
        'Запас хода',
        max_length=3
    )
    rating = models.FloatField(
        'Рейтинг автомобиля',
        max_length=2
    )
    coordinates = models.OneToOneField(
        CoordinatesCar,
        verbose_name='Координаты автомобиля',
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'

    def __str__(self):
        return f'[{self.company}]: {self.brand} {self.model}'
