from django.shortcuts import render
from .models import Timesheet
from JobCode.models import Job
from MachineMgt.models import Machine
from django.views.generic import ListView, CreateView, UpdateView


class TimesheetListView(ListView):
    model = Timesheet


class TimesheetCreateView(CreateView):
    model = Timesheet
    fields = [
        'site_code', 'contractor', 'date', 'total_hrs', 'total_amount',
        'status'
    ]

    def get_context_data(self, **kwargs):
        data = super(TimesheetCreateView, self).get_context_data(**kwargs)
        job = Job.objects.values_list('job_code', flat=True)
        jobrate = Job.objects.values_list('hourly_rate', flat=True).filter()
        machine = Machine.objects.values_list('machine_code', flat=True)
        data['job'] = job
        data['machine'] = machine
        return data


class TimesheetUpdateView(UpdateView):
    model = Timesheet
    template_name = 'Timecard/timesheet_status.html'
    fields = ['status']
