from django.core.management.base import BaseCommand
from apps.products.models import Product
from faker import Faker
import random

class Command(BaseCommand):
    help = 'Menghapus data lama dan mengisi database dengan 20 produk dummy baru'

    def handle(self, *args, **kwargs):
        fake = Faker()

        # 1. HAPUS SEMUA DATA LAMA
        self.stdout.write(self.style.WARNING('Membersihkan data produk lama...'))
        Product.objects.all().delete()
        
        self.stdout.write(self.style.SUCCESS('Data lama berhasil dihapus.'))

        # 2. ISI DATA BARU
        self.stdout.write('Sedang menyemai 20 data produk baru...')

        products_to_create = []
        for _ in range(20):
            # Gabungkan dua kata agar nama produk lebih unik
            product_name = f"{fake.word().capitalize()} {fake.word().capitalize()}"
            
            # Kita kumpulkan dalam list untuk bulk_create agar lebih cepat
            products_to_create.append(
                Product(
                    name=product_name,
                    price=random.randint(5, 100) * 1000,
                    stock=random.randint(1, 50)
                )
            )

        # Gunakan bulk_create untuk performa yang lebih baik di MySQL
        Product.objects.bulk_create(products_to_create)

        self.stdout.write(self.style.SUCCESS(f'Berhasil menyemai 20 data produk ke MySQL!'))