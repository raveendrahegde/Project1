from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=255)
    short_name = models.CharField(max_length=15)
    currency = models.CharField(max_length=15)
    corp_tax_rate = models.DecimalField(max_digits=3, decimal_places=2)

class StockExchange(models.Model):
    name = models.CharField(max_length=150)
    symbol = models.CharField(max_length=15)
    country = models.ForeignKey(Country)

class Company(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    stock_symbol = models.CharField(max_length=15, db_index=True)
    exchange = models.ForeignKey(StockExchange)
    stock_price = models.DecimalField(max_digits=12, decimal_places=2)
    refresh_time = models.DateTimeField()




