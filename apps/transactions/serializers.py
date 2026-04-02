from rest_framework import serializers
from .models import Transaction, TransactionItem

class TransactionItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionItem
        fields = ['product', 'quantity', 'subtotal']
        read_only_fields = ['subtotal']

class TransactionSerializer(serializers.ModelSerializer):
    items = TransactionItemSerializer(many=True)

    class Meta:
        model = Transaction
        fields = ['id', 'user', 'total_price', 'items', 'created_at']
        read_only_fields = ['total_price', 'user']