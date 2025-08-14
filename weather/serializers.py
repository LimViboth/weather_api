from rest_framework import serializers
from .models import City, WeatherRecord, FavoriteCity

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'

class WeatherSerializer(serializers.ModelSerializer):
    city = CitySerializer()

    class Meta:
        model = WeatherRecord
        fields = '__all__'

class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteCity
        fields = '__all__'
