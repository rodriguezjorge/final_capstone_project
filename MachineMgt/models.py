from django.db import models
from django.urls import reverse

class Machine(models.Model):
	machine_code = models.CharField(max_length=250, unique=True)
	description = models.TextField(blank=True)
	hourly_rent = models.DecimalField(max_digits=10, decimal_places=2)
	max_hour_per_day = models.IntegerField()
	def __str__(self):
		return '{}'.format(self.machine_code)
	def get_absolute_url(self):
		return reverse('machine-list')
