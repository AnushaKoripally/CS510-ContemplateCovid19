import pandas as pd
from django.shortcuts import render
import matplotlib.pyplot as plt

# Create your views here.
df3 = pd.read_json(
    'https://cdn.jsdelivr.net/gh/highcharts/highcharts@v7.0.0/samples/data/world-population-density.json')


def index(request):
    nursingHome = pd.read_csv('https://data.ct.gov/resource/wyn3-qphu.csv', encoding='utf-8', na_values=None)

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

def datasetAgeGenderEthnicity(request,selection):
    raceData = pd.read_csv('https://data.ct.gov/resource/7rne-efic.csv', encoding='utf-8', na_values=None)
    ageData = pd.read_csv('https://data.ct.gov/resource/ypz6-8qyf.csv', encoding='utf-8', na_values=None)
    genderData = pd.read_csv('https://data.ct.gov/resource/qa53-fghg.csv', encoding='utf-8', na_values=None)

    barplot = genderData[['gender',genderData.columns[3],genderData.columns[4],genderData.columns[7],genderData.columns[8]]].groupby('gender').sum().sort_values(by='gender')
    barplot = barplot.reset_index()
    print(barplot)

    barplotValMale = barplot[1:2].values.tolist().pop(0)
    barplotValMale = [x for x in barplotValMale if str(x) != 'Male']
    barplotValFemale = barplot[:1].values.tolist().pop(0)
    barplotValFemale = [x for x in barplotValFemale if str(x) != 'Female']
    barplotValOther = barplot[2:3].values.tolist().pop(0)
    barplotValOther = [x for x in barplotValOther if str(x) != 'Other']
    genderLabels = ['total_cases','confirmed_cases','total_deaths','confirmed_deaths']

    barplotage = ageData[['agegroups',ageData.columns[3],ageData.columns[4],ageData.columns[7],ageData.columns[8]]].groupby('agegroups').sum().sort_values(by='agegroups')
    barplotage = barplotage.reset_index()
    barplotage1 = barplotage[barplotage.columns[1]].values.tolist()
    barplotage2 = barplotage[barplotage.columns[2]].values.tolist()
    barplotage3 = barplotage[barplotage.columns[3]].values.tolist()
    barplotage4 = barplotage[barplotage.columns[4]].values.tolist()

    agesGrouped = barplotage['agegroups'].values.tolist()
    barplotage = barplotage.drop(['agegroups'], axis =1)
    barplotage.columns = ['','', '', '']

    print(barplotage)
    print(barplotage1)
    print(barplotage2)
    print(barplotage3)
    print(barplotage4)
    labels = ['total_cases','confirmed_cases','total_deaths','confirmed_deaths']
    print(agesGrouped)

    barplotrace = raceData[['hisp_race',raceData.columns[2],raceData.columns[3],raceData.columns[6]]].groupby('hisp_race').sum().sort_values(by='hisp_race')
    barplotrace = barplotrace.reset_index()
    print(barplotrace)
    barplotrace2 = barplotrace[barplotrace.columns[2]].values.tolist()
    barplotrace3 = barplotrace[barplotrace.columns[3]].values.tolist()
    racesGrouped = barplotrace['hisp_race'].values.tolist()
    print(racesGrouped)
    barplotrace = barplotrace.drop(['hisp_race'], axis =1)

    barplotrace.columns = ['', '', '']
    print(barplotrace2)
    print(barplotrace3)


    context = {'selection': selection, 'barplotValMale':barplotValMale, 'barplotValFemale':barplotValFemale,'barplotValOther':barplotValOther,'labels':genderLabels,
               'barplotage1':barplotage1,'barplotage2':barplotage2,'barplotage3':barplotage3,'barplotage4':barplotage4,'agesGrouped':agesGrouped,
               'barplotrace2':barplotrace2, 'barplotrace3':barplotrace3,'racesGrouped':racesGrouped}

    if selection == 'Gender':
        print(selection)
        return render(request, 'GenderCases.html', context)

    elif selection == 'Age':
        print(selection)
        return render(request, 'GenderCases.html', context)

    elif selection == 'Ethnicity':
        print(selection)
        return render(request, 'GenderCases.html', context)

def ageGenderEthnicityView(request):
    return render(request, 'AgeGenderEthnicityCases.html')
