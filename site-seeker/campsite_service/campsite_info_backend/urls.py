from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CampsiteViewSet, AvailabilityViewSet

router = DefaultRouter()
router.register(r'campsites', CampsiteViewSet)
router.register(r'availabilities', AvailabilityViewSet)


urlpatterns = [
    path('', include(router.urls)),
    ]
