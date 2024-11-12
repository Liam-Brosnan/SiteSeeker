from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from datetime import timedelta
from .models import Campsite, Availability
from .serializers import CampsiteSerializer, \
    AvailabilitySerializer, \
    UpdateAvailabilitySerializer
from .publisher import send_booking_message
import uuid


class CampsiteViewSet(viewsets.ModelViewSet):
    queryset = Campsite.objects.all()
    serializer_class = CampsiteSerializer

    @action(detail=True, methods=['get'],
            url_path='details',
            url_name='details')
    def details(self, request, pk=None):
        """
        A fucntion to retrieve all campsites in the database.
        """
        try:
            campsite = self.get_object()
            serializer = self.get_serializer(campsite)
            return Response(serializer.data)
        except Campsite.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @action(detail=True, methods=['get'],
            url_path='detail',
            url_name='detail')
    def detail(self, request, pk=None):
        """
        A function to retrieve a single campsite's information.
        """
        try:
            campsite = self.get_object()
            serializer = Campsite.objects.get(id=campsite.campsite_id)
            campsite_data = CampsiteSerializer(serializer).campsite_data
            return Response(campsite_data)
        except Campsite.DoesNotExist:
            return Response(
                {'error': 'Campsite not found'},
                status=status.HTTP_404_NOT_FOUND)


class AvailabilityViewSet(viewsets.ModelViewSet):
    queryset = Availability.objects.all()
    serializer_class = AvailabilitySerializer

    @action(detail=False, methods=['post'],
            url_path='update-availability',
            url_name='update-availability')
    def update_availability(self, request):
        """
        A function taht updates the availabiilty of a campsite by the number
        of people booking.
        """
        serializer = UpdateAvailabilitySerializer(data=request.data)
        if serializer.is_valid():
            campsite_id = serializer.validated_data['campsite_id']
            start_date = serializer.validated_data['start_date']
            end_date = serializer.validated_data['end_date']
            number_of_people = serializer.validated_data['number_of_people']

            try:
                campsite = Campsite.objects.get(id=campsite_id)
                current_date = start_date
                while current_date <= end_date:
                    availability = Availability.objects.get(
                        campsite=campsite, date=current_date)
                    if availability.available_capacity < number_of_people:
                        return Response(
                            {'error': 'Not enough capacity'},
                            status=status.HTTP_400_BAD_REQUEST)

                    availability.available_capacity -= number_of_people
                    availability.save()
                    current_date += timedelta(days=1)

                booking_id = str(uuid.uuid4())
                booking_data = {
                    'booking_id': booking_id,
                    'campsite_id': campsite_id,
                    'check_in_date': start_date.isoformat(),
                    'check_out_date': end_date.isoformat(),
                    'number_of_people': number_of_people,
                }
                send_booking_message(booking_data)

                return Response(
                    {
                        'status': 'Availability updated successfully',
                        'booking_id': booking_id
                    })

            except Availability.DoesNotExist:
                return Response(
                    {'error': 'Availability not found'},
                    status=status.HTTP_404_NOT_FOUND)
            except Campsite.DoesNotExist:
                return Response(
                    {'error': 'Campsite not found'},
                    status=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                return Response(
                    {'error': str(e)},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
