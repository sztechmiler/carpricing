from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('all', views.alldata, name='all'),
    path('all2', views.alldata2, name='all2'),
    path('', views.pricingModel, name='all2'),

]

urlpatterns += [
    path('<str:brand_name>', views.getBrandModelsNames, name='getBrandModelsNames'),
]