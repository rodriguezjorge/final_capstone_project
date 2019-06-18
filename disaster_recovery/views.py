from django.shortcuts import render
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import UserRegisterForm
from django.contrib.auth.mixins import LoginRequiredMixin

from JobCode.models import Job
from Timecard .models import Timesheet
from django.views.generic import ListView

class IndexView(LoginRequiredMixin,TemplateView):
    template_name = 'JobCode/index.html'

    def get_context_data(self, **kwargs):
         context = super(IndexView, self).get_context_data(**kwargs)
         context['job_list'] = Job.objects.all()
         context['timesheet_list'] = Timesheet.objects.all()
         return context



def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')

            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'JobCode/register.html', {'form': form})
