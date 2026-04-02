from django.db import transaction
from .models import Transaction, TransactionItem

class POSService:
    @staticmethod
    @transaction.atomic  
    def create_sale(user, items_data):
        total = 0
        sale = Transaction.objects.create(user=user)
        
        for item in items_data:
            product = item['product']
            qty = item['quantity']
            
            # Cek Stok
            if product.stock < qty:
                raise Exception(f"Stok {product.name} tidak cukup!")
            
            # Kurangi Stok
            product.stock -= qty
            product.save()
            
            # Hitung Subtotal
            subtotal = product.price * qty
            total += subtotal
            
            TransactionItem.objects.create(
                transaction=sale,
                product=product,
                quantity=qty,
                subtotal=subtotal
            )
            
        sale.total_price = total
        sale.save()
        return sale