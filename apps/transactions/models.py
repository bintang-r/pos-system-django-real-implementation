from django.db import models
from django.conf import settings
from apps.products.models import Product # Ini sudah benar jika Product ada di models.py produk

class Transaction(models.Model):
    # Gunakan settings.AUTH_USER_MODEL agar selalu sinkron dengan setting kita
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)

class TransactionItem(models.Model):
    transaction = models.ForeignKey(Transaction, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    subtotal = models.DecimalField(max_digits=12, decimal_places=2)