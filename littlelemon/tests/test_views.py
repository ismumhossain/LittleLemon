from django.test import TestCase
from restaurant.models import Menu
from rest_framework import status
from rest_framework.test import APIClient

class MenuViewTest(TestCase):

    def setUp(self):
        Menu.objects.create(title="IceCream", price=80, inventory=100)
        Menu.objects.create(title="Chicken", price=40, inventory=90)
        Menu.objects.create(title="Salad", price=60, inventory=70)

    def test_getall(self):
        client = APIClient()
        response = client.get('/restaurant/menu/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertEqual(len(data), 3)
        for item in data:
            self.assertIn('title', item)
            self.assertIn('price', item)
            self.assertIn('inventory', item)