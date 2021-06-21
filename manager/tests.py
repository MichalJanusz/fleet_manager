import random
from datetime import timedelta

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from mixer.backend.django import mixer
from rest_framework import status
from rest_framework.test import APITestCase

from manager.models import Flight, Aircraft


# Create your tests here.

class TestApi(APITestCase):

    @classmethod
    def setUpTestData(cls):
        cls.flights = []
        cls.aircrafts = mixer.cycle(10).blend(Aircraft)

        for _ in range(15):
            flight = mixer.blend(Flight, aircraft=random.choice(cls.aircrafts))
            cls.flights.append(flight)

    def test_list_aircrafts(self):
        path = reverse('aircraft-list')
        response = self.client.get(path)

        self.assertEquals(status.HTTP_200_OK, response.status_code)
        self.assertEquals(len(self.aircrafts), len(response.data))

    def test_list_flights(self):
        path = reverse('flight-list')
        response = self.client.get(path)

        self.assertEquals(status.HTTP_200_OK, response.status_code)
        self.assertEquals(len(self.flights), len(response.data))

    def test_post_aircraft(self):
        path = reverse('aircraft-list')
        test_data = {'serial': 'PL82710', 'manufacturer': 'Cessna'}
        response = self.client.post(path, data=test_data)

        self.assertEquals(status.HTTP_201_CREATED, response.status_code)
        del response.data['id']
        self.assertEquals(test_data, response.data)

    def test_post_flight(self):
        path = reverse('flight-list')
        now = timezone.now() + timedelta(minutes=15)
        future = now + timedelta(hours=5)
        test_data = {'departure_icao': 'ABCD', 'arrival_icao': 'CDBA', 'departure_time': now,
                     'arrival_time': future,
                     'aircraft': random.choice(self.aircrafts).pk}
        response = self.client.post(path, data=test_data)
        self.assertEquals(status.HTTP_201_CREATED, response.status_code)
        del response.data['id'], response.data['arrival_time'], response.data['departure_time'], test_data[
            'arrival_time'], test_data['departure_time']
        self.assertEquals(test_data, response.data)
