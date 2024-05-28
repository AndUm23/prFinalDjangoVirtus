from django.urls import include, path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register(r'tables', TableViewSet, basename='tables')
router.register(r'restaurantss', RestaurantViewSet, basename='restaurants')
router.register(r'orders', OrderViewSet, basename='orders')
router.register(r'bills', BillViewSet, basename='bills')

urlpatterns = [
    path('', include(router.urls)),
    #path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
]

urlpatterns += router.urls
#urlpatterns = format_suffix_patterns(urlpatterns)