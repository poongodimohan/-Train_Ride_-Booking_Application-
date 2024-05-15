from django.test import TestCase
from django.contrib.auth.models import User
from train_ticket_booking.models import Station, Route, RouteStation, Train, PassengerInfo
from train_ticket_booking.serializers import ReservationSerializer

class ReservationSerializerTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.station_a = Station.objects.create(name="Station A")
        self.station_b = Station.objects.create(name="Station B")
        self.route = Route.objects.create(start_station=self.station_a, end_station=self.station_b, distance=100, duration=2)
        self.train = Train.objects.create(train_name="Express", number="123", route=self.route, capacity=200, departure_time="08:00:00", arrival_time="10:00:00")
        self.route_station_a = RouteStation.objects.create(route=self.route, station=self.station_a, order=1)
        self.route_station_b = RouteStation.objects.create(route=self.route, station=self.station_b, order=2)
        self.passenger_info = PassengerInfo.objects.create(passenger_name=self.user, age=25, gender='male', phone_number='1234567890', address='123, Test Street')

    def test_valid_reservation_serializer(self):
        data = {
            'train': self.train.pk,
            'passengerinfo': self.passenger_info.pk,
            'source_station': self.station_a.pk,
            'destination_station': self.station_b.pk,
            'departure_date': '2024-05-15',
        }
        serializer = ReservationSerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_invalid_reservation_serializer(self):
        # Invalid because source_station comes after destination_station in route order
        data = {
            'train': self.train.pk,
            'passengerinfo': self.passenger_info.pk,
            'source_station': self.station_b.pk,
            'destination_station': self.station_a.pk,
            'departure_date': '2024-05-15',
        }
        serializer = ReservationSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('station', serializer.errors)
