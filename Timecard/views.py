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


def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        form = request.POST
        mydict = dict(form.lists())
        hrs_list = [int(i) for i in mydict['mytext1']]
        hrs_sum = sum(map(int, mydict['mytext1']))
        droplist = []
        for i in mydict['dropdown1']:
            q = Job.objects.values_list('hourly_rate',
                                        flat=True).filter(job_code__iexact=i)
            droplist.append(q[0])
        for i in mydict['dropdown2']:
            q = Machine.objects.values_list(
                'hourly_rent', flat=True).filter(machine_code__iexact=i)
            droplist.append(q[0])
        total_list = [x * y for x, y in zip(hrs_list, droplist)]
        total_sum = sum(total_list)

        ts = Timesheet()
        ts.site_code = mydict['site_code'][0]
        ts.date = mydict['date'][0]
        ts.contractor = mydict['contractor'][0]
        ts.total_hrs = hrs_sum
        ts.total_amount = total_sum
        ts.save()

    return render(request, 'Timecard/output_form.html', {'form': form})


class TimesheetUpdateView(UpdateView):
    model = Timesheet
    template_name = 'Timecard/timesheet_status.html'
    fields = ['status']
