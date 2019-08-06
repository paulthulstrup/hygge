from django.db import models
from django.utils.timezone import now

# Create your models here.
# Fields:
#   - Method of meeting
#   - Contact (Phone)

class Stock(models.Model):
    ticker = models.CharField(max_length=3)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.ticker

class User(models.Model):
    name = models.CharField(max_length=50)
    cashBalance = models.IntegerField()

    def __str__(self):
        return self.name


class TargetAllocation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    allocPercentage = models.IntegerField(default=0)

    def __str__(self):
        return self.stock.ticker + ": allocation = " + str(self.allocPercentage)+ "%"

