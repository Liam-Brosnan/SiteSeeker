from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Booking
from .serializers import BookingSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    @action(detail=True, methods=['get'])
    def details(self, request, pk=None):
        """
        A function to retrieve booking information.
        """
        try:
            booking = self.get_object()
            serializer = Booking.objects.get(id=booking.booking_id)
            booking_data = BookingSerializer(serializer).booking_data
            return Response(booking_data)
        except Booking.DoesNotExist:
            return Response(
                {'error': 'Booking not found'},
                status=status.HTTP_404_NOT_FOUND)
