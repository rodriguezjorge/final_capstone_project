from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomePage.as_view(), name="home"),
    path('timecard/', include('Timecard.urls')),
    path('jobcode/', include('JobCode.urls')),
    path('machinemgt/', include('MachineMgt.urls')),
    path('login/',
         auth_views.LoginView.as_view(template_name='JobCode/login.html'),
         name='login'),
    path('logout/',
         auth_views.LogoutView.as_view(template_name='JobCode/logout.html'),
         name='logout'),
]
