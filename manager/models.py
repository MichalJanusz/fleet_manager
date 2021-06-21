from django.db import models


# Create your models here.

class Aircraft(models.Model):
    serial = models.CharField(unique=True, max_length=128)
    manufacturer = models.CharField(max_length=64)

    def __str__(self):
        return self.serial


class Flight(models.Model):
    departure_icao = models.CharField(max_length=4)
    arrival_icao = models.CharField(max_length=4)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    aircraft = models.ForeignKey('Aircraft', null=True, blank=True, on_delete=models.SET_NULL, related_name='flights')

    def __str__(self):
        return f'Flight from {self.departure_icao} to {self.arrival_icao} ID:{self.id}'
