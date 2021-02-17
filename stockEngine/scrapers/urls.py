from django.urls import path
from scrapers.views import news_list_api_view

urlpatterns = [
    path('news/', news_list_api_view, name='news-list')
]