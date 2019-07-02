from django.db import models

class Stock(models.Model):
    name = models.CharField(max_length=100, blank=False)
    quantity = models.IntegerField()
    cost = models.FloatField()
    measurement = models.CharField(max_length=20)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('created_on',)