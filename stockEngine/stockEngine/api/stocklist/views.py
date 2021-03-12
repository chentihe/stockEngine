from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics

from stockEngine.api.stocklist.models import StockList
from stockEngine.api.stocklist.serializers import StockListSerializer

class StockListView(generics.RetrieveAPIView):
    serializer_class = StockListSerializer
    permission_classes = (IsAuthenticated,)
    queryset = StockList.objects.all()
    lookup_field = 'stock_no'
    lookup_url_kwarg = 'stock_no'

    def get_queryset(self):
        kwargs = self.kwargs.get('stock_no')
        return StockList.objects.filter(stock_no=kwargs)