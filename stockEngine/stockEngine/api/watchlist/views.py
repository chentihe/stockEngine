from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, filters

from stockEngine.api.watchlist.models import WatchList
from stockEngine.api.watchlist.serializers import WatchListSerializer

class WatchListView(viewsets.ModelViewSet):
    serializer_class = WatchListSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'stock_no'
    filter_backends = (filters.SearchFilter,)
    search_fields = ('stock_no__stock_no', 'stock_no__stock_name')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        user = self.request.user
        watchlist = WatchList.objects.filter(user=user).order_by('stock_no')
        return watchlist