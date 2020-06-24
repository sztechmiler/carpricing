from rest_framework import routers
from rental import api_views as rental_views
router = routers.DefaultRouter()
router.register(r’friends’, rental_views.FriedViewSet)