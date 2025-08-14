from django.contrib import admin
from .models import City, WeatherRecord, FavoriteCity

admin.site.register(City)
admin.site.register(WeatherRecord)
admin.site.register(FavoriteCity)
