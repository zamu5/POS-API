from rest_framework.test import APITestCase
from .models import Item


class ItemTest(APITestCase):
    def setUp(self):
        self.item_1 = Item.objects.create(
            description="Hamburger",
            price=4.5,
            quantity=6
        )
        self.item_2 = Item.objects.create(
            description="fries",
            price=2.8,
            quantity=9
        )

    def test_list_items_status_code(self):
        response = self.client.get(f'/menu/')
        self.assertEqual(response.status_code, 200)

    def test_item_detail_status_code(self):
        response = self.client.get(f'/menu/detail/{self.item_1.id}/')
        self.assertEqual(response.status_code, 200)

    def test_item_detail_response(self):
        response = self.client.get(f'/menu/detail/{self.item_1.id}/')
        data = {
            "id": 1,
            "description": "Hamburger",
            "price": 4.5,
            "quantity": 6
        }
        self.assertEqual(response.data, data)


