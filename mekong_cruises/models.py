from django.db import models

# Create your models here.

class Journey(models.Model):

    JOURNEY_TYPE_CHOICES = [
        ('day', 'Day Cruise'),
        ('night', 'Night Cruise'),
        ('festival', 'Festival Day Cruise'),
    ]
    CURRENCY_CHOICES = [
        ('usd', 'USD'),
        ('riel', 'Riel'),
    ]

    name = models.CharField(max_length=200, blank=True, default='')
    type = models.CharField(max_length=20, choices=JOURNEY_TYPE_CHOICES, default='day')
    date = models.DateField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=4, choices=CURRENCY_CHOICES, default='usd')
    seats_required = models.IntegerField(default=1)
    description = models.TextField(max_length=2000,blank=True, default='')

    def __str__(self):
        return f"{self.name} ({self.get_type_display()})"
