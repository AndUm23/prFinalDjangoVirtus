from rest_framework import serializers
from .models import *

from rest_framework.response import Response
from datetime import datetime

class RestaurantSerializerModel(serializers.ModelSerializer):       
    class Meta:
        model = Restaurant
        fields = "__all__"
        
class OrderSerializerModel(serializers.ModelSerializer):       
    class Meta:
        model = Order
        fields = "__all__"
        
class TableSerializerModel(serializers.ModelSerializer):       
    class Meta:
        model = Table
        fields = "__all__"
        
class BillSerializerModel(serializers.ModelSerializer):       
    class Meta:
        model = Bill
        fields = "__all__"

class ShiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shift
        fields = ['start_date', 'end_date', 'restaurant'] 
   
class Tables_restaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tables_restaurant
        fields = "__all__"