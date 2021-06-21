from django_filters import rest_framework as filters, DateTimeFromToRangeFilter

from manager.models import Flight


class FlightFilterSet(filters.FilterSet):
    departure_time = DateTimeFromToRangeFilter()

    class Meta:
        model = Flight
        fields = ['departure_time', 'departure_icao', 'arrival_icao']
