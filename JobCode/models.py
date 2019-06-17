from django.db import models
from django.urls import reverse


class Job(models.Model):
    job_code = models.CharField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    hourly_rate = models.DecimalField(max_digits=10, decimal_places=2)
    max_hour_per_day = models.IntegerField()

    def __str__(self):
        return '{}'.format(self.job_code)

    def get_absolute_url(self):
        return reverse('job-list')
