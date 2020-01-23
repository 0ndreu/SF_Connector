from django.urls import reverse
from rest_framework.test import APITestCase
from .models import Vacancy
from .serializers import VacancySerializer
from rest_framework import status


class BlogTest(APITestCase):

    def test_post(self):
        response = self.client.post('')
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_patch(self):
        response = self.client.patch('')
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_get(self):
        response = self.client.get('')
        self.assertEquals(response.status_code, status.HTTP_200_OK)

