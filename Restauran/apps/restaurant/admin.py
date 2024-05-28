from django.contrib import admin
from .models import *


# Register your models here.

class RestaurantAdmin(admin.ModelAdmin):
    list_display=["id", "name", "direcction", "owner"]
    
class ProductAdmin(admin.ModelAdmin):
    list_display=["id", "name", "cost_per_unit", "all_restaurants"]    

class TableAdmin(admin.ModelAdmin):
    list_display=["id", "number", "PersonCapacity"] 
    
class WaiterAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_first_name', 'user_last_name', 'charge')
    
    def user_first_name(self, obj):
        return obj.user.first_name
    user_first_name.short_description = 'First Name'
    
    def user_last_name(self, obj):
        return obj.user.last_name
    user_last_name.short_description = 'Last Name'
    
class BillAdmin(admin.ModelAdmin):
    list_display=["id", "cost", "tip_porcent", "final_cost"]   

class OrderAdmin(admin.ModelAdmin):
    list_display=["id", "waiter", "tableR"]
    
class tables_restaurantAdmin(admin.ModelAdmin):
    list_display=["id", "table", "restaurant"]
    
class products_orderAdmin(admin.ModelAdmin):
    list_display=["id", "product", "order"]
 
class products_restaurantAdmin(admin.ModelAdmin):
    list_display=["id", "product", "restaurant"]
  
class ShiftAdmin(admin.ModelAdmin):
    list_display=["id", "waiter", "start_date", "end_date", "restaurant"]

class Tip_WaiterAdmin(admin.ModelAdmin):
    list_display=["id", "bill", "waiter", "paid"]

admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Table,TableAdmin)
admin.site.register(Order,OrderAdmin)
admin.site.register(Waiter,WaiterAdmin)
admin.site.register(Bill,BillAdmin)
admin.site.register(Tables_restaurant,tables_restaurantAdmin)
admin.site.register(products_order,products_orderAdmin)
admin.site.register(products_restaurant,products_restaurantAdmin)
admin.site.register(Shift,ShiftAdmin)
admin.site.register(Tip_Waiter,Tip_WaiterAdmin)
