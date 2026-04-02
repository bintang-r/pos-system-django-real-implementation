from rest_framework.views import APIView
from rest_framework.response import Response
from .services import POSService
from .serializers import TransactionSerializer

class CheckoutView(APIView):
    def post(self, request):
        # Logika pemanggilan service
        try:
            sale = POSService.create_sale(request.user, request.data['items'])
            return Response({"message": "Transaksi Sukses", "id": sale.id})
        except Exception as e:
            return Response({"error": str(e)}, status=400)