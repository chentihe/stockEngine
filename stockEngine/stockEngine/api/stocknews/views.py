from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics

from stockEngine.api.stocknews.models import StockNews
from stockEngine.api.stocknews.serializers import StockNewsSerializer

class StockNewsDetailView(generics.ListAPIView):
    serializer_class = StockNewsSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'stock_no'
    lookup_url_kwarg = 'stock_no'

    def get_queryset(self):
        kwargs = self.kwargs.get('stock_no')
        return StockNews.objects.filter(stock_no=kwargs).order_by('-published_at')