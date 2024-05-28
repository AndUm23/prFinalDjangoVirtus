from rest_framework import serializers
from .models import *

class ProductSerializerModel(serializers.ModelSerializer):       
    class Meta:
        model = Product
        fields = "__all__"
        
