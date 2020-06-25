from rest_framework import serializers
from .models import CarBrand, CarModel

class CarbrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarBrand
        fields='__all__'


class CarmodelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields='__all__'

