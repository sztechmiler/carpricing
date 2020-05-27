from django.shortcuts import render
from django.http import JsonResponse
from .forms import updateForm, GetPriceForm

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

