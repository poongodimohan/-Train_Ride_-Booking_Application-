from django.test import TestCase
from django.contrib.auth.models import User
from train_ticket_booking.models import Station, Route, RouteStation, Train, PassengerInfo, Reservation
from django.utils import timezone
import uuid

class ModelsTestCase(TestCase):
    def setUp(self):
        self.station = Station.objects.create(name="Station A")
        self.route = Route.objects.create(start_station="Station A", end_station="Station B", distance=100, duration=2)
        self.train = Train.objects.create(train_name="Express", number="123", route=self.route, capacity=200, departure_time="08:00:00", arrival_time="10:00:00")
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.passenger_info = PassengerInfo.objects.create(passenger_name=self.user, age=25, gender='male', phone_number='1234567890', address='123, Test Street')
        self.reservation = Reservation.objects.create(train=self.train, passengerinfo=self.passenger_info, source_station=self.station, destination_station=self.station, departure_date=timezone.now(), booking_date=timezone.now(), ticket_number=uuid.uuid4().hex, status='booked')

    def test_station_str(self):
        self.assertEqual(str(self.station), "Station A")

    def test_route_str(self):
        self.assertEqual(str(self.route), "Station A-Station B-100-2-<QuerySet [<Station: Station A>]>")


    def test_route_station_str(self):
        route_station = RouteStation.objects.create(route=self.route, station=self.station, order=1)
        self.assertEqual(str(route_station), "Station A- Station: Station A, Order: 1")

    def test_train_str(self):
        self.assertEqual(str(self.train), "Express (123) - Route: Station A-Station B-100-2 - Departure: 08:00:00 - Arrival: 10:00:00")

    def test_passenger_info_str(self):
        self.assertEqual(str(self.passenger_info), "testuser-25-male-1234567890-123, Test Street")

    def test_reservation_str(self):
        self.assertEqual(str(self.reservation), f"{self.train}-{self.passenger_info}-{self.station}-{self.station}-{timezone.now().date()}-{timezone.now()}-{self.reservation.ticket_number}-booked")
