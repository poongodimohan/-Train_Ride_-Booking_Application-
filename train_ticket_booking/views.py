from rest_framework import viewsets
from .models import Route, RouteStation, Train, PassengerInfo, Reservation, Station
from .serializers import (
    StationSerializer,
    RouteSerializer,
    RouteStationSerializer,
    TrainSerializer,
    PassengerInfoSerializer,
    ReservationSerializer,
    UserSerializer
)
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin
from django.contrib.auth import get_user_model



class CreateUserView(CreateModelMixin, GenericViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class Routeview(viewsets.ModelViewSet):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
    http_method_names = ["get", "post", "put", "delete"]



class RouteStationView(viewsets.ModelViewSet):
    queryset = RouteStation.objects.all()
    serializer_class = RouteStationSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
    http_method_names = ["get", "post", "put", "delete"]



class TrainView(viewsets.ModelViewSet):
    queryset = Train.objects.all()
    serializer_class = TrainSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
    http_method_names = ["get", "post", "put", "delete"]



class PassengerInfoView(viewsets.ModelViewSet):
    queryset = PassengerInfo.objects.all()
    serializer_class = PassengerInfoSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
    http_method_names = ["get", "post", "put", "delete"]



class ReservationView(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
    http_method_names = ["get", "post", "put", "delete"]



class StationView(viewsets.ModelViewSet):
    queryset = Station.objects.all()
    serializer_class = StationSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
    http_method_names = ["get", "post", "put", "delete"]

