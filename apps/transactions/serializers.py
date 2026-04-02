from rest_framework import serializers
from .models import Transaction, TransactionItem

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionItem
        fields = ['product', 'quantity']

class TransactionSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True)

    class Meta:
        model = Transaction
        fields = ['id', 'total_price', 'items', 'created_at']