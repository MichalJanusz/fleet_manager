from datetime import datetime

from django.utils import timezone

from rest_framework import serializers
from manager.models import Aircraft, Flight


# Serializers are written here


class AircraftSerializer(serializers.ModelSerializer):

    def validate(self, data):

        data['serial'] = data['serial'].upper()
        return data

    class Meta:
        model = Aircraft
        fields = '__all__'


class FlightSerializer(serializers.ModelSerializer):

    def validate(self, data):

        if data['departure_time'] < timezone.now():
            raise serializers.ValidationError({'departure_time': 'Departure time has to be in future!'})

        if data['departure_time'] > data['arrival_time']:
            raise serializers.ValidationError({'arrival_time': 'Arrival time must be after departure time!'})

        data['departure_icao'] = data['departure_icao'].upper()
        data['arrival_icao'] = data['arrival_icao'].upper()

        return data

    class Meta:
        model = Flight
        fields = '__all__'
