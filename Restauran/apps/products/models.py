from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=60, null=False, blank=False)
    cost_per_unit = models.FloatField(null=False, blank=False)
    all_restaurants=models.BooleanField(default=True)