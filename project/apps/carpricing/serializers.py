from rest_framework import serlializers
from .models import model

class CarbrandSerializer(serlializers.ModelSerializer):
    class Meta:
        model = model.CarBrand

class CarmodelSerializer(serlializers.ModelSerializer):
    class Meta:
        model = model.CarModel