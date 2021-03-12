from django.urls import include, path
from rest_framework.routers import DefaultRouter
from stockEngine.api.watchlist.views import WatchListView

router = DefaultRouter()
router.register(r'watchlist', WatchListView, basename='watchlist')

urlpatterns = [
    path('', include(router.urls))
]