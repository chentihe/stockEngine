from rest_framework import serializers

from stockEngine.api.stocklist.models import StockList

class StockListSerializer(serializers.ModelSerializer):

    class Meta:
        model = StockList
        fields = '__all__'