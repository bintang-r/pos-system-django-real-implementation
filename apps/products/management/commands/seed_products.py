from django.core.management.base import BaseCommand
from faker import Faker
from apps.products.models import Product
import random
from faker import Faker

class Command(BaseCommand):
    help = 'Mengisi database dengan data produk dummy'

    fake = Faker()

    def handle(self, *args, **kwargs):
        for _ in range(20): 
            Product.objects.create(
                name=self.fake.word().capitalize() + " " + self.fake.word(),
                price=random.randint(5, 100) * 1000,
            stock=random.randint(1, 50)
        )