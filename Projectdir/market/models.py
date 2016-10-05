from django.db import models

class Currency(models.Model):
    name = models.CharField(max_length=35)
    symbol = models.CharField(max_length=5)
    dollar_value = models.DecimalField(max_digits=12, decimal_places=2)

class Country(models.Model):
    name = models.CharField(max_length=225)
    short_name = models.CharField(max_length=15)
    currency = models.ForeignKey(Currency)
    corp_tax_rate = models.DecimalField(max_digits=5, decimal_places=2)

class Place(models.Model):
    name = models.CharField(max_length=55)
    country = models.ForeignKey(Country)

class StockExchange(models.Model):
    name = models.CharField(max_length=150)
    symbol = models.CharField(max_length=15)
    headquarter = models.ForeignKey(Place)
    open = models.TimeField()
    close = models.TimeField()
    primary_economy = models.ForeignKey(Country)

class Company(models.Model):
    name = models.CharField(max_length=225)
    headquarter = models.ForeignKey(Place)
    description = models.TextField()
    ceo = models.CharField(max_length=35) #Could be an independent entity

class Company2Exchange(models.Model):
    company = models.ForeignKey(Company)
    exchange = models.ForeignKey(StockExchange)
    symbol = models.CharField(max_length=15)
    stock_price = models.DecimalField(max_digits=12, decimal_places=2)
    refresh_time = models.DateTimeField()




