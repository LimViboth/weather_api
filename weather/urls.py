from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CityViewSet, WeatherViewSet, FavoriteViewSet

router = DefaultRouter()
router.register(r'cities', CityViewSet)
router.register(r'weather', WeatherViewSet)
router.register(r'favorites', FavoriteViewSet, basename='favorite')

urlpatterns = [
    path('', include(router.urls)),
]
