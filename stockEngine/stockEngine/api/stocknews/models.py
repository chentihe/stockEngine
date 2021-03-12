from django.db import models

class StockNews(models.Model):
    stock_no = models.CharField(max_length=255)
    title = models.CharField(max_length=255, blank=True, null=True)
    link = models.CharField(max_length=255, blank=True, null=True)
    published_at = models.CharField(max_length=255, blank=True, null=True)
    source = models.CharField(max_length=255, blank=True, null=True)