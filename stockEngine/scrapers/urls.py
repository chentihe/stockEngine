from django.urls import path
from scrapers.views import news_detail_api_view

urlpatterns = [
    path('news/<int:stock_no>/', news_detail_api_view, name='news-list'),
]