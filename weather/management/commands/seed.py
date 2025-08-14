from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from weather.models import City, WeatherRecord, FavoriteCity
from datetime import date, timedelta
import random

class Command(BaseCommand):
    help = 'Seed the database with sample users, cities, weather records and favorites.'

    def handle(self, *args, **options):
        self.stdout.write('Seeding database...')

        # Create users
        users = []
        for i in range(1, 4):
            username = f'user{i}'
            user, created = User.objects.get_or_create(username=username)
            if created:
                user.set_password('password')
                user.save()
            users.append(user)

        # Create cities
        city_data = [
            ('Cairo', 'EG'),
            ('Tokyo', 'JP'),
            ('New York', 'US'),
            ('London', 'GB'),
            ('Paris', 'FR'),
        ]
        cities = []
        for name, country in city_data:
            city, _ = City.objects.get_or_create(name=name, country=country)
            cities.append(city)

        # Create weather records for the last 7 days for each city
        for city in cities:
            for d in range(7):
                record_date = date.today() - timedelta(days=d)
                temp = round(random.uniform(-5, 40), 1)
                humidity = random.randint(10, 100)
                condition = random.choice(['Sunny', 'Cloudy', 'Rain', 'Snow', 'Windy'])
                WeatherRecord.objects.get_or_create(
                    city=city,
                    date=record_date,
                    defaults={'temperature': temp, 'humidity': humidity, 'condition': condition}
                )

        # Create favorites: each user favorites two random cities
        for user in users:
            favs = random.sample(cities, 2)
            for city in favs:
                FavoriteCity.objects.get_or_create(user=user, city=city)

        self.stdout.write(self.style.SUCCESS('Seeding complete.'))
