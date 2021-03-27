from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
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

def datasets(request):
    nursingHome = pd.read_csv('https://data.ct.gov/resource/wyn3-qphu.csv', encoding='utf-8', na_values=None)
    barplot = nursingHome[['town', nursingHome.columns[4], nursingHome.columns[5], nursingHome.columns[6],
                           nursingHome.columns[7]]].groupby('town').sum().sort_values(by='town',
                                                                                      ascending=True)
    barplot = barplot.reset_index()
    barplot.columns = ['town', 'values', 'values1', 'values2', 'values3']
    barplotval = barplot['values'].values.tolist()
    barplotval1 = barplot['values1'].values.tolist()
    barplotval2 = barplot['values2'].values.tolist()
    barplotval3 = barplot['values3'].values.tolist()
    towns = barplot['town'].values.tolist()
    showNursing = 'False'
    context = {'town': towns, 'barplotval': barplotval, 'barplotval1': barplotval1, 'barplotval2': barplotval2,
               'barplotval3': barplotval3, 'showNursing' : showNursing }
    return render(request, 'index2.html', context)



