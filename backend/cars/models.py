from django.db import models


class EngineType(models.Model):
    """
    Модель для представления типов двигателей автомобилей.
    """

    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class CarType(models.Model):
    """
    Модель для представления типов автомобилей.
    """

    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


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

    is_available = models.BooleanField(default=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    engine_type = models.ForeignKey(EngineType, on_delete=models.CASCADE)
    car_type = models.ForeignKey(CarType, on_delete=models.CASCADE)
    rating = models.IntegerField()
    coefficient = models.IntegerField()
    child_seat = models.BooleanField()
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return f"{self.company} {self.name} {self.model}"
