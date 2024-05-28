from django.db import models

#Import from othr apps
from apps.users.models import User, Waiter
from apps.products.models import Product

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=60, null=False, blank=False)
    direcction = models.CharField(max_length=80, null=False, blank=False)
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    
    def __str__(self) -> str:
        return self.name
    
class Table(models.Model):
    number = models.IntegerField(null=False, blank=False)
    PersonCapacity = models.IntegerField(null=False, blank=False)
    
    def save(self, *args, **kwargs) -> None:
        self.id = self.number
        return super().save(*args, **kwargs)
    
class Tables_restaurant(models.Model):
    table = models.OneToOneField(Table, on_delete=models.DO_NOTHING)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.DO_NOTHING)

class Order(models.Model):
    waiter = models.ForeignKey(Waiter, on_delete=models.DO_NOTHING)
    tableR = models.ForeignKey(Tables_restaurant, on_delete=models.DO_NOTHING)
   
class products_order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    order = models.ForeignKey(Order, on_delete=models.DO_NOTHING)
    
class products_restaurant(models.Model):
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.DO_NOTHING)
    
class Bill(models.Model):
    order = models.OneToOneField(Order, on_delete=models.DO_NOTHING)
    cost = models.FloatField(null=False, blank=False)
    tip_porcent = models.FloatField(null=False, blank=False)
    
    @property
    def final_cost(self):
        return self.cost + (self.cost*(self.tip_porcent/100.00))
    
class Shift(models.Model):
    waiter = models.ForeignKey(Waiter, on_delete=models.DO_NOTHING)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    restaurant = models.ForeignKey(Restaurant, on_delete=models.DO_NOTHING)
    
class Tip_Waiter(models.Model):
    bill = models.OneToOneField(Bill, on_delete=models.DO_NOTHING)
    waiter = models.ForeignKey(Waiter, on_delete=models.DO_NOTHING)
    paid = models.BooleanField(default=False)


    