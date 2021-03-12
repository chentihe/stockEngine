from django.db import models

class StockList(models.Model):
    stock_no = models.CharField(primary_key=True, max_length=255)
    stock_name = models.CharField(max_length=255)

    def __str__(self):
        return self.stock_no