from rest_framework import routers
from .apps.carpricing import views as cars_views
router = routers.DefaultRouter()
router.register(r"friends", cars_views.CarBrandViewSet)