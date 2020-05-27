"""carpricing URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import RedirectView
from .apps.carpricing import views
from .apps.api import views as api_views



urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/', include('project.apps.api.urls',namespace='api')),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# Add URL maps to redirect the base URL to our application
urlpatterns += [
    path('', views.index, name='index'),
    path('api/', include('project.apps.api.urls')),
    # path('api/all', api_views.alldata, name = 'czekolada' )
]
