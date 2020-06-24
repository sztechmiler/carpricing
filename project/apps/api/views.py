from django.shortcuts import render
from django.http import JsonResponse
from django.views import generic
from project.apps.carpricing.models import CarBrand, CarModel

# Create your views here.
def alldata(request):
    data = {
        'name': "Greg",
        "location": "Rudy",
        "is_active": True,
        "count": 33
    }
    return JsonResponse(data)

def alldata2(request):
    data = {
        'name': "Greg2",
        "location": "Rudy2",
        "is_active": False,
        "count": 332
    }
    return JsonResponse(data)

def pricingModel(request):
    model_name = request.GET.get('Model', '')
    marka_name = request.GET.get('Marka', '')

    data = {
        'model_name': model_name,
        "marka_name": marka_name,
        "is_active": True,
        "count": 1454545
    }
    return JsonResponse(data)

#just added

class BrandModels(generic.DetailView):
    model = CarBrand

    def get_queryset(self):
        return CarBrand.objects.filter(name__icontains='Opel')[:5]  # Get 5 books containing the title war

def getBrandModelsNames(request, brand_name):
    brand = CarBrand.objects.get(name = brand_name)
    brandModels = CarModel.objects.filter(car_brand = brand).values("name")
    brandModelsNames = []
    for model in brandModels:
        brandModelsNames.append(model.get("name"))

    data = {
        'brandModels': brandModelsNames,
    }
    return JsonResponse(data)