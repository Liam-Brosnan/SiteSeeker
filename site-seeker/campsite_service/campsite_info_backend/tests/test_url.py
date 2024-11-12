from django.urls import reverse, resolve
from django.test import SimpleTestCase
from rest_framework.test import APIClient
from campsite_info_backend.views import CampsiteViewSet, AvailabilityViewSet


class TestUrls(SimpleTestCase):
    def setUp(self):
        self.client = APIClient()

    def test_campsites_url_resolve(self):
        url = reverse('campsite-list')
        self.assertEqual(resolve(url).func.cls, CampsiteViewSet)

    def test_availabiilties_url_resolves(self):
        url = reverse('availability-list')
        self.assertEqual(resolve(url).func.cls, AvailabilityViewSet)
