import uuid

from django.db import models

# Create your models here.
from django.urls import reverse


# Create your models here.
class CarBrand(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        """String for representing the Model object."""
        return self.name


class CarModel(models.Model):
    name = models.CharField(max_length=200)
    car_brand = models.ForeignKey(CarBrand, on_delete=models.SET_NULL, null=True)


    def __str__(self):
        """String for representing the Model object."""
        return self.name
