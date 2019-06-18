from django.urls import path
from . import views
from .views import TimesheetListView, TimesheetCreateView, TimesheetUpdateView, get_name

urlpatterns = [
    path('', TimesheetListView.as_view(), name='timesheet-list'),
    path('timesheet/new/',
         TimesheetCreateView.as_view(),
         name='timesheet-create'),
    path('timesheet/<int:pk>/update/',
         TimesheetUpdateView.as_view(),
         name='timesheet-update'),
    path('timesheet/new/time', views.get_name, name='time'),
]
