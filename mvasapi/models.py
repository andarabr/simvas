from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Transaction(models.Model):
    transaction_id = models.CharField(max_length=11)
    transaction_date = models.CharField(max_length=15)
    corporate_id = models.CharField(max_length=4)
    corporate_name = models.CharField(max_length=56)
    platform = models.CharField(max_length=25)
    deal_type = models.CharField(max_length=8)
    direction = models.CharField(max_length=12)
    base_currency = models.CharField(max_length=3)
    quote_currency = models.CharField(max_length=3)
    base_volume = models.FloatField()
    quote_volume = models.FloatField()
    periods = models.IntegerField()
    near_rate = models.FloatField()
    far_rate = models.FloatField(null=True)
    near_value_date = models.CharField(max_length=15)
    far_value_date = models.CharField(max_length=15, null=True)
    confirmed_at = models.CharField(max_length=15)
    confirmed_by = models.CharField(max_length=30)
    trader_id = models.CharField(max_length=10)
    trader_name = models.CharField(max_length=20)
    transaction_purpose = models.CharField(max_length=40, null=True)

def __str__(self):
    """Return a string representation of the model."""
    return self.transaction_id