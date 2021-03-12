from django.urls import path
from stockEngine.api.stocknews.views import StockNewsDetailView

urlpatterns = [
    path('news/<str:stock_no>/', StockNewsDetailView.as_view(), name='news-detail'),
    # path('stock/<int:stock_no>/', stock_price_api_view, name='stock-price')
]