"""coronaDashPage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

import patterns as patterns
from django.contrib import admin
from django.urls import path, include, re_path
from firstPage import views
from django.conf.urls import url
from django.views.generic.base import RedirectView



urlpatterns = [
   path('admin/', admin.site.urls),
   path(r'', views.index, name='Mainpage'),
   path(r'^$', views.index, name='Mainpage'),
   path(r'Home', views.index, name='Mainpage'),
   url(r'^NursingHome', views.datasets1, name='NursingHome'),
   url(r'^CasesbyCounty', views.maps, name='CasesbyCounty'),
   url(r'^CasesbyTown', views.townMap, name='CasesbyTown'),
   url(r'^VaccinationbyCounty', views.vaccination, name='VaccinationbyCounty'),
   url(r'^schools', views.schoolCases, name='schools'),
   url(r'casesByAgeGenderEthnicity', views.ageGenderEthnicityView, name='AgeGenderEthnicity'),
   url(r'specimenCollection', views.specimen, name='specimenCollection'),
   url(r'100kPopulation', views.population, name='100kPopulation'),
   url(r'^AgeGenderEthnicitySelection/(?P<selection>\w+)/$', views.datasetAgeGenderEthnicity,  name='AgeGenderEthnicitySelection'),

   url(r'^TownSelection/(?P<town_selection>\w+)/$', views.datasets, name='TownSelection'),
   re_path(r'^.*/CasesbyTown', RedirectView.as_view(url='http://127.0.0.1:8000/CasesbyTown', permanent=False),  name='index'),
   re_path(r'^.*/NursingHome', RedirectView.as_view(url='http://127.0.0.1:8000/NursingHome', permanent=False),   name='index'),
   re_path(r'^.*/CasesbyCounty', RedirectView.as_view(url='http://127.0.0.1:8000/CasesbyCounty', permanent=False),  name='index'),
   re_path(r'^.*/VaccinationbyCounty', RedirectView.as_view(url='http://127.0.0.1:8000/VaccinationbyCounty', permanent=False), name='index'),
   re_path(r'^.*/schools', RedirectView.as_view(url='http://127.0.0.1:8000/schools', permanent=False), name='index'),
   re_path(r'^.*/Home', RedirectView.as_view(url='http://127.0.0.1:8000/Home', permanent=False), name='index'),
   re_path(r'^.*/specimenCollection', RedirectView.as_view(url='http://127.0.0.1:8000/specimenCollection', permanent=False), name='index'),
   re_path(r'^.*/100kPopulation', RedirectView.as_view(url='http://127.0.0.1:8000/100kPopulation', permanent=False), name='index'),

]