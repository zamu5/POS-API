from django.db import models


class Item(models.Model):
    description = models.TextField()
    price = models.FloatField()
    quantity = models.IntegerField()

    class Meta:
        verbose_name_plural = 'ietms'
