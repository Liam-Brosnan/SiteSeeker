from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Campsite, Availability
from datetime import timedelta


@receiver(post_save, sender=Campsite)
def update_availability(sender, instance, **kwargs):
    campsite = instance.campsite
    current_date = instance.start_date
    while current_date <= instance.end_date:
        availability_record, created = Availability.objects.get_or_create(
            campsite=campsite, date=current_date)
        availability_record.available_capacity -= instance.number_of_people
        availability_record.save()
        current_date += timedelta(days=1)
