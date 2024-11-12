from django.db import models


class Campsite(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    capacity = models.IntegerField()
    amenities = models.CharField(max_length=100, default='')
    description = models.CharField(max_length=1000, default='')

    def __str__(self):
        return self.name


class Availability(models.Model):
    campsite = models.ForeignKey(Campsite, on_delete=models.CASCADE)
    date = models.DateField()
    available_capacity = models.IntegerField()

    class Meta:
        unique_together = ('campsite', 'date')

    def __str__(self):
        return f'{self.campsite.name} on {self.date} - \
                {self.available_capacity} sports left'
