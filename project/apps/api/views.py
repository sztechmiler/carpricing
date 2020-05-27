from django.shortcuts import render
from django.http import JsonResponse


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
