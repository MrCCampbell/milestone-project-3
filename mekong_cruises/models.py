from django.db import models

# Create your models here.

class Journey(models.Model):

    JOURNEY_TYPE_CHOICES = [
        ('day', 'Day Cruise 09.00AM - 16.00PM'),
        ('night', 'Night Cruise 17.00PM - 22.00PM'),
        ('festival', 'Day Festival Cruise 09.00AM - 16.00PM'),
        ('night_festival', 'Night Festival Cruise 17.00PM - 22.00PM'),
    ]
    TIME_SLOTS_CHOICES = [
        ('09.00', '09:00AM'),
        ('10.00', '10:00AM'),
        ('11.00', '11:00AM'),
        ('12.00', '12:00PM'),
        ('13.00', '13:00PM'),
        ('14.00', '14:00PM'),
        ('15.00', '15:00PM'),
        ('16.00', '16:00PM'),
        ('17.00', '17:00PM'),
        ('18.00', '18:00PM'),
        ('19.00', '19:00PM'),
        ('20.00', '20:00PM'),
        ('21.00', '21:00PM'),
        ('22.00', '22:00PM'),
    ]
    PRICE_CHOICES = [
        ('15.00', '$15.00 Standard Day (approx. 62,000 Riel)'),
        ('20.00', '$20.00 Standard Night (approx. 80,000 Riel)'),
        ('25.00', '$25.00 Festival Day (approx. 100,000 Riel)'),
        ('30.00', '$30.00 Festival Night (approx. 120,000 Riel)'),
    ]
    PAYMENT_CHOICES = [
        ('cash', 'Cash'),   
        ('bank', 'Bank Quick Transfer'),
    ]

    name = models.CharField(max_length=200, blank=True, default='')
    type = models.CharField(max_length=20, choices=JOURNEY_TYPE_CHOICES, default='day')
    date = models.DateField(blank=True, null=True)
    time_slots = models.CharField(max_length=5, choices=TIME_SLOTS_CHOICES, default='09.00')
    price = models.CharField(max_length=10, choices=PRICE_CHOICES, default='15.00')
    seats_required = models.IntegerField(default=1)
    requests = models.TextField(max_length= 500, blank=True, default='')
    payment_type = models.CharField(max_length=10, choices=PAYMENT_CHOICES, blank=True, default='cash')

    def __str__(self):
        return f"{self.name} ({self.get_type_display})"
