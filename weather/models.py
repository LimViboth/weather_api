from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class City(models.Model):
    name = models.CharField(max_length=100, unique=True)
    country = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}, {self.country}"

class WeatherRecord(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name="weather_records")
    date = models.DateField()
    temperature = models.FloatField()
    humidity = models.IntegerField()
    condition = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.city.name} - {self.date}"

class FavoriteCity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'city')

    def __str__(self):
        return f"{self.user.username} -> {self.city.name}"
