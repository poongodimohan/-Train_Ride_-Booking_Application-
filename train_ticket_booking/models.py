from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import uuid


class Station(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "station"


class Route(models.Model):
    start_station = models.CharField(max_length=50)
    end_station = models.CharField(max_length=50)
    distance = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.FloatField()
    station = models.ManyToManyField(Station, related_name="routes")

    def __str__(self):
        return f"{self.start_station}-{self.end_station}-{self.distance}-{self.duration}-{self. station}"

    class Meta:
        db_table = "route"


class RouteStation(models.Model):
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    station = models.ForeignKey("Station", on_delete=models.CASCADE)
    order = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.route} - Station: {self.station}, Order: {self.order}"

    class Meta:
        unique_together = ("route", "station")

        ordering = ["order"]


class Train(models.Model):
    train_name = models.CharField(max_length=100)
    number = models.CharField(max_length=20)
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    capacity = models.PositiveIntegerField()
    departure_time = models.TimeField()
    arrival_time = models.TimeField()

    def __str__(self):
        return f"{self.train_name} ({self.number}) - Route: {self.route} - Departure: {self.departure_time} - Arrival: {self.arrival_time}"

    class Meta:
        db_table = "train"


class PassengerInfo(models.Model):
    passenger_name = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.PositiveIntegerField()
    gender = models.CharField(
        max_length=10,
        choices=(("male", "Male"), ("female", "Female"), ("other", "Other")),
    )
    phone_number = models.CharField(max_length=10)
    address = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.passenger_name}-{self.age}-{self.gender}-{self.phone_number}-{self.address}"

    class Meta:
        db_table = "passengerInfo"


class Reservation(models.Model):
    train = models.ForeignKey(Train, on_delete=models.CASCADE)
    passengerinfo = models.ForeignKey(PassengerInfo, on_delete=models.CASCADE)
    source_station = models.ForeignKey(
        "Station", related_name="source_reservation", on_delete=models.CASCADE
    )
    destination_station = models.ForeignKey(
        "Station", related_name="destination_reservations", on_delete=models.CASCADE
    )
    departure_date = models.DateField()

    booking_date = models.DateTimeField(default=timezone.now)

    ticket_number = models.CharField(max_length=20, unique=True, blank=True)
    status = models.CharField(
        max_length=20,
        choices=(("booked", "Booked"), ("cancelled", "Cancelled")),
        default="booked",
    )

    def save(self, *args, **kwargs):
        if not self.id:
            self.ticket_number = uuid.uuid4().hex
        super(Reservation, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.train}-{self.passengerinfo}-{self.source_station}-{self. destination_station}-{self.departure_date }-{self.booking_date}-{self.ticket_number}-{self.status}"

    class Meta:
        db_table = "reservation"
