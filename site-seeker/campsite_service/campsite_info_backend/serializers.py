from rest_framework import serializers
from .models import Campsite, Availability


class CampsiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campsite
        fields = '__all__'


class AvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Availability
        fields = '__all__'


class UpdateAvailabilitySerializer(serializers.Serializer):
    campsite_id = serializers.IntegerField()
    start_date = serializers.DateField()
    end_date = serializers.DateField()
    number_of_people = serializers.IntegerField()
