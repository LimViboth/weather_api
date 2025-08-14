from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import City, WeatherRecord, FavoriteCity
from .serializers import CitySerializer, WeatherSerializer, FavoriteSerializer
from .permissions import IsAdminOrReadOnly

class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes = [IsAdminOrReadOnly]

class WeatherViewSet(viewsets.ModelViewSet):
    queryset = WeatherRecord.objects.all()
    serializer_class = WeatherSerializer
    permission_classes = [IsAdminOrReadOnly]

class FavoriteViewSet(viewsets.ModelViewSet):
    serializer_class = FavoriteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return FavoriteCity.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
