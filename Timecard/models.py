from django.db import models
from django.urls import reverse
import datetime


class Timesheet(models.Model):
    site_code = models.CharField(max_length=250)
    contractor = models.CharField(max_length=250, blank=True)
    total_amount = models.DecimalField(max_digits=20, decimal_places=2)
    total_hrs = models.PositiveIntegerField()
    date = models.DateField(default=datetime.date.today)
    status = models.BooleanField(default=False)

    def __str__(self):
        return '{}'.format(self.site_code)

    def get_absolute_url(self):
        return reverse('timesheet-list')


# class LaborEntry(models.Model):
#     pass
#     site_code = models.CharField(max_length=250, unique=True)
#     contractor = models.CharField(max_length=250, blank=True)
#     total_amount = models.DecimalField(max_digits=20, decimal_places=2)
#     total_hrs = models.PositiveIntegerField()
#     date = models.DateField(default=datetime.date.today)
#     status = models.BooleanField(default=False)

#     def __str__(self):
#         return '{}'.format(self.site_code)

#     def get_absolute_url(self):
#         return reverse('labor-list')


# class MachineEntry(models.Model):
#     pass

#     def __str__(self):
#         return '{}'.format(self.site_code)

#     def get_absolute_url(self):
#         return reverse('machine-list')


# # Create your models here.
