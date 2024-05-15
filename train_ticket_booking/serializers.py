from rest_framework import serializers
from .models import Route, RouteStation, Train, PassengerInfo, Reservation, Station
from django.contrib.auth.models import User

from django.contrib.auth import get_user_model

UserModel = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = UserModel.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        )
        return user

    class Meta:
        model = UserModel
        fields = ('password', 'username', 'first_name', 'last_name',)


class RouteStationSerializer(serializers.ModelSerializer):
    class Meta:
        model = RouteStation
        fields = "__all__"


class StationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = "__all__"


class RouteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Route
        fields = "__all__"


class TrainSerializer(serializers.ModelSerializer):

    class Meta:
        model = Train
        fields = "__all__"


class PassengerInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = PassengerInfo
        fields = "__all__"


class ReservationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reservation
        fields = "__all__"

    def validate(self, data):
        
        # Get the id of source_staion,destination_station and train route id

        source_id = data.get("source_station").id
        destination_id = data.get("destination_station").id
        route_id = data.get("train").route_id

        # Find the route stations for the source and destination stations using the route ID

        source_station = RouteStation.objects.filter(
            route_id=route_id, station_id=source_id
        )
        desination_station = RouteStation.objects.filter(
            route_id=route_id, station_id=destination_id
        )

        # Validate the order of source and destination stations

        if source_station and desination_station:
            if source_station[0].order < desination_station[0].order:
                return data

        # If the order is not valid, raise validation error

        raise serializers.ValidationError({"station": "Invalid station order"})
