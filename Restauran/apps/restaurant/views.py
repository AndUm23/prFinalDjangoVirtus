from django.shortcuts import render, get_object_or_404

#other modules
from rest_framework.views import APIView
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated


#self modules
from .models import *
from .serializers import *
from .permissions import IsManager, IsManagerOrAdminTables

#utils
from datetime import datetime
# Create your views here.

class TableViewSet(viewsets.ModelViewSet):
    queryset = Table.objects.all()
    serializer_class = TableSerializerModel
    
class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializerModel
    
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializerModel 

    def destroy(self, request, *args, **kwargs):
        permission_classes = [IsAuthenticated, IsManagerOrAdminTables]
        # Check if the user is a Manager or AdminTables
        if request.user.charge not in ['MANAGER', 'ADMINTABLES']:
            return Response({"error": "You don't have permission to perform this action"}, status=403)
        return super().destroy(request, *args, **kwargs)


class BillViewSet(viewsets.ModelViewSet):
    queryset = Bill.objects.all()
    serializer_class = BillSerializerModel
    
    def destroy(self, request, *args, **kwargs):
        permission_classes = [IsAuthenticated, IsManager]
        # Check if the user is a Manager
        if not request.user.charge == 'MANAGER':
            return Response({"error": "You don't have permission to perform this action"}, status=403)
        return super().destroy(request, *args, **kwargs)
    


class AddShiftSet(viewsets.ModelViewSet):
    queryset = Shift.objects.all()
    serializer_class = ShiftSerializer
            
class AddShiftView(APIView):
    
    @action(detail=True, methods=['get'])
    def post(self, request, waiter_id, *args, **kwargs):
        waiter = get_object_or_404(Waiter, id=waiter_id)

        start_date_str = request.data.get('start_date')
        end_date_str = request.data.get('end_date')
        restaurant_id = request.data.get('restaurant')

        try:
            start_date = datetime.strptime(start_date_str, '%d-%m-%YT%H:%M:%S')
            end_date = datetime.strptime(end_date_str, '%d-%m-%YT%H:%M:%S')
            restaurant = Restaurant.objects.get(id=restaurant_id)

            shift = Shift.objects.create(
                waiter=waiter,
                start_date=start_date,
                end_date=end_date,
                restaurant=restaurant
            )

            serializer = ShiftSerializer(shift)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        except (Restaurant.DoesNotExist) as e:
            return Response({"error": "Error con Rest"}, status=status.HTTP_400_BAD_REQUEST)
 

    