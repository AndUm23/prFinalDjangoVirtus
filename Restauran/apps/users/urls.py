from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, WaiterViewSet
from apps.restaurant.views import AddShiftView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'waiters', WaiterViewSet)


urlpatterns = [
    path('', include(router.urls)),
]

urlpatterns += [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('waiters/<int:waiter_id>/add_shift/', AddShiftView.as_view(), name='add_shift')
]

urlpatterns += router.urls