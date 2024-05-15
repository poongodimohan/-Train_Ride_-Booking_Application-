from django.contrib import admin

from .models import Route, RouteStation, Train, PassengerInfo, Reservation, Station

admin.site.register([Route,
                     RouteStation, 
                     Train,
                     PassengerInfo,
                     Reservation,
                     Station])
