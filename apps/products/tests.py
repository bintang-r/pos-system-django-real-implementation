from django.test import TestCase
from .models import Product

class ProductModelTest(TestCase):
    def setUp(self):
        self.product = Product.objects.create(
            name="Kopi Susu",
            price=15000,
            stock=10
        )

    def test_product_content(self):
        self.assertEqual(self.product.name, "Kopi Susu")
        self.assertEqual(float(self.product.price), 15000.0)
        self.assertEqual(self.product.stock, 10)

    def test_str_representation(self):
        self.assertEqual(str(self.product), "Kopi Susu")