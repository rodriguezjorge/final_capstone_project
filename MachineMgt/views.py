from django.shortcuts import render
from . models import Machine
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView


class MachineListView(ListView):
    model=Machine

class MachineDetailView(DetailView):

    model=Machine

class MachineCreateView(CreateView):
    model=Machine
    fields = ['machine_code', 'description','hourly_rent','max_hour_per_day']

class MachineUpdateView(UpdateView):
    model=Machine

    fields = ['machine_code', 'description','hourly_rent','max_hour_per_day']

class MachineDeleteView(DeleteView):
    model=Machine
    success_url='/'
