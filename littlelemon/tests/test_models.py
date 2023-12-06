from django.test import TestCase
from restaurant.models import Menu

class MenuItemTest(TestCase):
    def test_get_name(self):
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        print(item)
        self.assertEqual(item.title, "IceCream")
        
    def test_get_price(self):
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        print(item)
        self.assertEqual(item.price, 80)
        
    def test_get_inventory(self):
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        print(item)
        self.assertEqual(item.inventory, 100)
        
    def test_get_item(self):
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        print(item)
        self.assertEqual(str(item), "IceCream : 80")
        