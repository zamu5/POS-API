from django.db import models


class Order(models.Model):
    items = models.JSONField()
    payment_amount = models.FloatField()
    note = models.CharField(max_length=250)

    class Meta:
        verbose_name_plural = 'orders'

