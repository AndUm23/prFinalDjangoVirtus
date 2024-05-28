from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models import Sum, F, ExpressionWrapper, FloatField
from datetime import datetime

from .serializers import WaiterSerializer, UserSerializer
from .models import Waiter
from apps.restaurant.models import Shift, Tip_Waiter, Restaurant, Tables_restaurant, Order
from apps.restaurant.serializers import ShiftSerializer, Tables_restaurantSerializer, OrderSerializerModel

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    

class WaiterViewSet(viewsets.ModelViewSet):
    queryset = Waiter.objects.all()
    serializer_class = WaiterSerializer
    
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data

        # Check if 'extra' parameter is in the request
        extra = request.query_params.get('extra')
        if extra == '1':
            now = timezone.now()
            shifts = Shift.objects.filter(waiter=instance.id, start_date__gte=now).order_by('start_date')[:5]
            shifts_serializer = ShiftSerializer(shifts, many=True)
            data['next_shifts'] = shifts_serializer.data

        return Response(data)
    
    
    @action(detail=True, methods=['get'])
    def get_Shifts(self, request, pk=None):
        waiter = self.get_object()          
        
        shifts = Shift.objects.filter(waiter=waiter)
        
        # Serializamos las tareas y las preparamos para la respuesta
        data = [
            {
                "id": shift.id,
                "waiter" : shift.waiter.user.first_name,
                "waiterLN" : shift.waiter.user.last_name,
                "start_date" : shift.start_date,
                "end_date" : shift.end_date, 
                "restaurant": shift.restaurant.name,
            }
            for shift in shifts
        ]
        
        return Response(data)
        
    @action(detail=True, methods=['get'])
    def get_tips(self, request, pk=None):
        waiter = self.get_object()
        tips = Tip_Waiter.objects.filter(waiter=waiter)
        
        final_cost_expression = ExpressionWrapper(
            (F('bill__cost') + (F('bill__cost') * F('bill__tip_porcent') / 100.0))-F('bill__cost'),
            output_field=FloatField()
        )

        total_tips_paid = tips.filter(paid=True).aggregate(total=Sum(final_cost_expression))['total'] or 0
        total_current_tips = tips.filter(paid=False).aggregate(total=Sum(final_cost_expression))['total'] or 0

        response_data = {
            "tips_paid": total_tips_paid,
            "current_tips": total_current_tips
        }

        return Response(response_data)
       
    @action(detail=True, methods=['post'])
    def add_Shift(self, request, *args, **kwargs):
        waiter = self.get_object()

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
       
    @action(detail=True, methods=['get'])
    def get_Tables(self, request, pk=None):
        waiter = self.get_object()          

        now = timezone.now()
        
        current_shift = Shift.objects.filter(
            waiter=waiter,
            start_date__lte=now,
            end_date__gte=now
        ).first()

        if current_shift:
            restaurant = current_shift.restaurant
            #tables = .objects.filter(restaurant=restaurant)
            tables_restaurant = Tables_restaurant.objects.filter(restaurant=restaurant)
        else:
            tables_restaurant = Tables_restaurant.objects.none()
            
        serializer = Tables_restaurantSerializer(tables_restaurant, many=True)
        return Response(serializer.data)
        
    @action(detail=True, methods=['get'])
    def orders(self, request, pk=None):
        waiter = self.get_object()
        active = request.query_params.get('active')

        if active == '1':
            orders = Order.objects.filter(waiter=waiter).exclude(bill__cost__isnull=False)
        else:
            orders = Order.objects.filter(waiter=waiter)
            print(55)

        serializer = OrderSerializerModel(orders, many=True)
        return Response(serializer.data) 
    
    
    