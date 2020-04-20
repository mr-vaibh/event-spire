from django.db import models
from django.utils import timezone

# Create your models here.

class Centre(models.Model):
    centre_name = models.CharField(max_length=50, default='', blank=False)
    centre_contact = models.CharField(max_length=20, default='', blank=True)
    centre_address = models.TextField(max_length=300, default='', blank=True)
    centre_img = models.ImageField(upload_to='home/centre/', blank=True)
    date_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.centre_name

class Event(models.Model):
    centre = models.ForeignKey(Centre, on_delete=models.CASCADE, default=None, null=False)
    event_name = models.CharField(max_length=50, default='', blank=True)
    start_date = models.DateField(blank=True)
    end_date = models.DateField(blank=True)
    faciliator = models.CharField(max_length=100, default='', blank=True)
    host = models.CharField(max_length=50, default='', blank=True)
    event_manager = models.CharField(max_length=50, default='', blank=True)
    event_contact = models.CharField(max_length=20, default='', blank=True)
    location = models.CharField(max_length=100, default='', blank=True)
    event_img = models.ImageField(upload_to='home/event/', blank=False)
    date_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(f'Event of - {self.centre}')