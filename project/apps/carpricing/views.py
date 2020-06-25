from django.shortcuts import render
from django.http import JsonResponse
from .forms import updateForm, GetPriceForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import CarModel, CarBrand

from rest_framework import viewsets
from . import serializers


def index(request):
    jakasdana = ['asada', 'basdasdaq']
    form = updateForm(initial={"some_data": "wartosc updatu"})
    query_form = GetPriceForm()
    context = {
        'cos1': {'coscos1', 'coscos2'},
        'cos2': 2,
        'cos3': 'jakistest',
        'cos4': jakasdana,
        'form': form,
        'query_form': query_form,
    }
    return render(request, 'index.html', context=context)

class CarmodelCreate(CreateView):
    model = CarModel
    fields = '__all__'

class CarbrandCreate(CreateView):
    model = CarBrand
    fields = '__all__'

class CarBrandViewSet(viewsets.ModelViewSet):
    queryset = CarBrand.objects.all()
    serializer_class = serializers.CarbrandSerializer