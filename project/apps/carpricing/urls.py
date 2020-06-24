from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import RedirectView
from .views import CarmodelCreate, CarbrandCreate


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/', include('api.urls',namespace='api')),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += [
    path('', RedirectView.as_view(url='/web/', permanent=True)),
    path('carmodel/create/', CarmodelCreate.as_view(), name='carmodel_create'),
    path('carbrand/create/', CarbrandCreate.as_view(), name='carmodel_create'),


]

