from django.test import TestCase
from django.contrib.auth import get_user_model
from apps.products.models import Product
from .models import Transaction
from .services import POSService

User = get_user_model()

class TransactionServiceTest(TestCase):
    def setUp(self):
        # Siapkan User, Produk, dan Stok
        self.user = User.objects.create_user(username="kasir_test", password="123")
        self.product = Product.objects.create(name="Snack", price=5000, stock=5)

    def test_create_sale_success(self):
        """Tes transaksi berhasil dan stok berkurang"""
        items_data = [
            {'product': self.product, 'quantity': 2}
        ]
        
        # Jalankan service
        sale = POSService.create_sale(self.user, items_data)
        
        # Cek Total Harga (5000 * 2 = 10000)
        self.assertEqual(sale.total_price, 10000)
        
        # Cek Stok Berkurang (5 - 2 = 3)
        self.product.refresh_from_db()
        self.assertEqual(self.product.stock, 3)

    def test_create_sale_insufficient_stock(self):
        """Tes transaksi gagal jika stok tidak cukup"""
        items_data = [
            {'product': self.product, 'quantity': 10} # Stok hanya 5
        ]
        
        with self.assertRaises(Exception) as context:
            POSService.create_sale(self.user, items_data)
        
        self.assertIn("tidak cukup", str(context.exception))
        
        # Pastikan tidak ada transaksi yang tersimpan di DB
        self.assertEqual(Transaction.objects.count(), 0)