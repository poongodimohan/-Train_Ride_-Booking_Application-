from django.urls import path, include


from rest_framework.routers import DefaultRouter
from .views import (
    Routeview,
    RouteStationView,
    TrainView,
    PassengerInfoView,
    ReservationView,
    StationView,
    CreateUserView
)

# Initialize the DefaultRouter
router = DefaultRouter()


router.register("route", Routeview, basename="route")
router.register("routeStation", RouteStationView, "routeStation")
router.register("train", TrainView, basename="train")
router.register("passengerInfo", PassengerInfoView, "passengerInfo")
router.register("reservation", ReservationView, "reservation")
router.register("station", StationView, "station")
router.register("user", CreateUserView)



urlpatterns = [
    path("", include(router.urls)),
    
]

