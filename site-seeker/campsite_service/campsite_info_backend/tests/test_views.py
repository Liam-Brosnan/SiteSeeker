from rest_framework.test import APITestCase
from rest_framework import status
from campsite_info_backend.models import Campsite


class CampsiteViewSetTests(APITestCase):
    def setUp(self):
        self.campsite = Campsite.objects.create(
            id='1',
            name="Test Campsite",
            location="Test Location",
            capacity=10,
            amenities="Test Amenities",
            description="Test Description",
        )
        self.client = self.client

    def test_details_view(self):
        url = f'/api/campsite/{self.campsite.id}/detials/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], self.campsite.id)
