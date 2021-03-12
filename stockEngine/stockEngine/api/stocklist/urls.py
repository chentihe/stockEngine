from django.urls import path
from stockEngine.api.stocklist.views import StockListView

urlpatterns = [
    path('stock/<str:stock_no>/', StockListView.as_view(), name='stock-detail'),
]