from rest_framework import serializers

from stockEngine.api.stocklist.serializers import StockListSerializer
from stockEngine.api.watchlist.models import WatchList

class WatchListSerializer(serializers.ModelSerializer):
    stock_name = serializers.SerializerMethodField()

    class Meta:
        model = WatchList
        fields = ['stock_no', 'stock_name']

    def get_stock_name(self, instance):
        return instance.stock_no.stock_name