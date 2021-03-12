from rest_framework import serializers

from stockEngine.api.stocknews.models import StockNews

class StockNewsSerializer(serializers.ModelSerializer):

    class Meta:
        model = StockNews
        fields = '__all__'