from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
import os
import numpy as np

# Create your views here.
df3 = pd.read_json(
    'https://cdn.jsdelivr.net/gh/highcharts/highcharts@v7.0.0/samples/data/world-population-density.json')


def index(request):
    nursingHome = pd.read_csv('https://data.ct.gov/resource/wyn3-qphu.csv', encoding='utf-8', na_values=None)
    """barplot = nursingHome[['town', nursingHome.columns[4]]].groupby('town').sum().sort_values(by='licensed_beds',ascending=False)
    barplot = barplot.reset_index()
    barplot.columns = ['town', 'values']
    barplotval = barplot['values'].values.tolist()
    towns = barplot['town'].values.tolist()"""

    barplot = nursingHome[['town', nursingHome.columns[4], nursingHome.columns[5], nursingHome.columns[6],
                           nursingHome.columns[7]]].groupby('town').sum().sort_values(by='licensed_beds',
                                                                                      ascending=False)
    barplot = barplot.reset_index()
    barplot.columns = ['town', 'values', 'values1', 'values2', 'values3']
    barplotval = barplot['values'].values.tolist()
    barplotval1 = barplot['values1'].values.tolist()
    barplotval2 = barplot['values2'].values.tolist()
    barplotval3 = barplot['values3'].values.tolist()
    towns = barplot['town'].values.tolist()
    DailyUpdate = pd.read_csv('https://raw.githubusercontent.com/nytimes/covid-19-data/master/live/us-states.csv', encoding='utf-8', na_values=None)
    value = DailyUpdate.loc[DailyUpdate['state'].isin(["Connecticut"])]
    value = value[['state', value.columns[2], value.columns[3], value.columns[4],
                        value.columns[5], value.columns[6]]]

    allData = []
    for i in range(value.shape[0]):
        temp = value.iloc[i]
        allData.append(dict(temp))


    showNursing = 'True'
    context = {'data' : allData, 'showNursing':showNursing }
    return render(request, 'index.html', context)

def index1(request):
    DailyUpdate = pd.read_csv('https://raw.githubusercontent.com/nytimes/covid-19-data/master/live/us-states.csv', encoding='utf-8', na_values=None)
    value = DailyUpdate.loc[DailyUpdate['state'].isin(["Connecticut"])]

    value = value[[ value.columns[0], 'state', value.columns[2], value.columns[3], value.columns[4],
                        value.columns[5], value.columns[6]]]

    allData = []
    for i in range(value.shape[0]):
        temp = value.iloc[i]
        allData.append(dict(temp))


    showNursing = 'True'
    context = {'data' : allData, 'showNursing':showNursing }
    return render(request, 'index.html', context)

def datasets(request, town_selection):
    nursingHome = pd.read_csv('https://data.ct.gov/resource/wyn3-qphu.csv', encoding='utf-8', na_values=None)
    barplot = nursingHome[['town', nursingHome.columns[4], nursingHome.columns[5], nursingHome.columns[6],
                           nursingHome.columns[7]]].groupby('town').sum().sort_values(by='town',
                                                                                      ascending=True)


    barplot = barplot.reset_index()
    barplot.columns = ['town', 'licensed_beds', 'residents_with_covid', 'covid_19_associated_lab_confirmed', 'covid_19_associated_deaths_probable']
    towns = barplot['town'].values.tolist()
    filterbarplot = barplot['town']==town_selection
    barplot.where(filterbarplot, inplace=True)
    barplotval = barplot['licensed_beds'].values.tolist()
    barplotval = [x for x in barplotval if str(x) != 'nan']
    barplotval1 = barplot['residents_with_covid'].values.tolist()
    barplotval1 = [x for x in barplotval1 if str(x) != 'nan']
    barplotval2 = barplot['covid_19_associated_lab_confirmed'].values.tolist()
    barplotval2 = [x for x in barplotval2 if str(x) != 'nan']
    barplotval3 = barplot['covid_19_associated_deaths_probable'].values.tolist()
    barplotval3 = [x for x in barplotval3 if str(x) != 'nan']
    showNursing = 'False'
    fields = ['licensed_beds', 'residents_with_covid', 'covid_19_associated_lab_confirmed', 'covid_19_associated_deaths_probable']
    context = {'town': towns, 'barplotval': barplotval, 'barplotval1': barplotval1, 'barplotval2': barplotval2,
               'barplotval3': barplotval3, 'showNursing': showNursing, 'fields':fields, 'town_selection':town_selection}
    print(town_selection)
    print(barplotval)
    print(barplotval1)
    print(barplotval2)
    print(barplotval3)

    return render(request, 'index3.html', context)

def datasets1(request):
    nursingHome = pd.read_csv('https://data.ct.gov/resource/wyn3-qphu.csv', encoding='utf-8', na_values=None)
    barplot = nursingHome[['town']].groupby('town').sum().sort_values(by='town',ascending=True)
    barplot = barplot.reset_index()
    barplot.columns = ['town']
    showNursing = 'False'
    showTownSelection ='False'
    town_selection='None'
    towns = barplot['town'].values.tolist()
    context = {'town': towns,'showNursing': showNursing, 'showTownSelection':showTownSelection, 'town_selection':town_selection}
    return render(request, 'index2.html', context)


