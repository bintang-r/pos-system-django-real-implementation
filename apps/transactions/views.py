from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .services import POSService
from .serializers import TransactionSerializer

class CheckoutView(APIView):
    def post(self, request):
        items_data = request.data.get('items', [])
        if not items_data:
            return Response({"error": "Keranjang kosong"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Memanggil logic dari Service Layer yang sudah kita buat sebelumnya
            sale = POSService.create_sale(request.user, items_data)
            serializer = TransactionSerializer(sale)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)