from django.db import models
from bookings.models import Booking
# Create your models here.


class CruiseHire(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    cruise_line = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    cruise_name = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    departure_port = models.CharField(max_length=100, blank=True, null=True)
    email_contact = models.CharField(max_length=100, blank=True, null=True)
    dep_date = models.DateField(null=True, blank=True)
    dep_time = models.DateField(max_length=100, blank=True, null=True)
    telephone_contact = models.CharField(max_length=100, blank=True, null=True)
    return_date = models.DateField(null=True, blank=True)
    return_time = models.CharField(max_length=100, blank=True, null=True)
    return_port = models.CharField(max_length=100, blank=True, null=True)
    duration = models.FloatField(null=True, blank=True)
    num_rooms = models.FloatField(null=True, blank=True)
    state_room = models.CharField(max_length=100, null=True, blank=True)
    category = models.CharField(max_length=100, null=True, blank=True)
    type = models.CharField(max_length=100, null=True, blank=True)
    meal_plan = models.CharField(max_length=100, null=True, blank=True)
    num_guests = models.FloatField(default=0, null=True, blank=True)
    net_per_night = models.FloatField(null=True, blank=True)
    net_per_stay = models.FloatField(null=True, blank=True)
    gross_per_night = models.FloatField(null=True, blank=True)
    gross_per_stay = models.FloatField(null=True, blank=True)
    notes = models.CharField(max_length=100, null=True, blank=True)
    supplier = models.CharField(max_length=100, null=True, blank=True)
    supplier_ref = models.CharField(max_length=100, null=True, blank=True)
    booking_date = models.DateField(null=True, blank=True)
    booked_by = models.CharField(max_length=100, null=True, blank=True)
    cancellation_date = models.DateField(null=True, blank=True)
    deposit_paid = models.FloatField(default=0.0)
    payment_due = models.FloatField(default=0.0)
    payment_method = models.CharField(null=True, blank=True, max_length=100)
    balance_due_date = models.DateField(null=True, blank=True)
    vat_id = models.CharField(max_length=100, null=True, blank=True)

