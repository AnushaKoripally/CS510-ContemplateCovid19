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
from django.urls import path, include
from firstPage import views
from django.conf.urls import url


urlpatterns = [
   path('admin/', admin.site.urls),
   path(r'', views.index, name='Mainpage'),
   path(r'^$', views.index, name='Mainpage'),
   path(r'Home', views.index, name='Mainpage'),
   url(r'^NursingHome', views.datasets1, name='NursingHome'),
   url(r'^TownSelection/(?P<town_selection>\w+)/$', views.datasets, name='TownSelection'),
   #url(r'^TownSelection/(?P<town_selection>\w+)/$', views.datasets, name='TownSelection'),
]