from django.shortcuts import render
from . models import Job
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView


class JobListView(ListView):
    model=Job

class JobDetailView(DetailView):

    model=Job

class JobCreateView(CreateView):
    model=Job
    fields = ['job_code', 'description','hourly_rate','max_hour_per_day']

class JobUpdateView(UpdateView):
    model=Job

    fields = ['job_code', 'description','hourly_rate','max_hour_per_day']

class JobDeleteView(DeleteView):
    model=Job
    success_url='/'
