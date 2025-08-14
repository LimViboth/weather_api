from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework import status

class WeatherAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="test", password="1234")
        self.client.login(username="test", password="1234")

    def test_city_list(self):
        response = self.client.get("/api/cities/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
