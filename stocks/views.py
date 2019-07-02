from stocks.models import Stock
from stocks.serializers import StockSerializer
from rest_framework import generics


class StockList(generics.ListCreateAPIView):
    """
    List all sock products, or create a new stock
    """
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

class StockDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a stock
    """
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
        