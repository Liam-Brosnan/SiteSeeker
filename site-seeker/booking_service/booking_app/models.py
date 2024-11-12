from django.db import models


class Booking(models.Model):
    booking_id = models.UUIDField(
        primary_key=True, editable=False)
    campsite_id = models.IntegerField()
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    number_of_people = models.IntegerField()
