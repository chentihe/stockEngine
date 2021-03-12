from django.db import models
from users.models import CustomUser
from stockEngine.api.stocklist.models import StockList

class WatchList(models.Model):
    user = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE)
    stock_no = models.ForeignKey(to=StockList, on_delete=models.CASCADE)

    def __str__(self):
        return '%s put %s into watchlist' % (self.user, self.stock_no)