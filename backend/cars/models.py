import uuid
from django.db import models
from model_utils import Choices


CAR_TYPE = Choices(
    ('0', 'sedan'),
    ('1', 'hatchback'),
    ('2', 'minivan'),
    ('3', 'coupe'),
    ('4', 'universal'),
    ('5', 'other'),
)
ENGINE_TYPE = Choices(
    ('0', 'diesel'),
    ('1', 'electro'),
    ('2', 'benzine')
)
FUEL_LEVEL = Choices(
    ('0', 'Полный бак'),
    ('1', '100 км'),
    ('2', '50 км'),
)


class Company(models.Model):
    """
    Модель для представления компаний, производящих автомобили.
    """

    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Car(models.Model):
    """
    Модель для представления данных о конкретных автомобилях.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image = models.ImageField(upload_to='uploads/%Y/%m/%d/', null=True, blank=True)
    is_available = models.BooleanField(default=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    engine_type = models.CharField(max_length=1, choices=ENGINE_TYPE, default=ENGINE_TYPE['0'])
    car_type = models.CharField(max_length=1, choices=CAR_TYPE, default=CAR_TYPE['0'])
    rating = models.FloatField()
    coefficient = models.IntegerField()
    child_seat = models.BooleanField()
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    fuel_level = models.CharField(max_length=1, choices=FUEL_LEVEL, default=FUEL_LEVEL['0'])
    price = models.FloatField()

    def __str__(self):
        return f"{self.company} {self.name} {self.model}"
