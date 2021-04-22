from django.shortcuts import render, redirect
from django.http import HttpResponse
from collections import OrderedDict
import pandas as pd
import os
import numpy as np

def index(request):
    DailyUpdate = pd.read_csv('https://api.covidtracking.com/v1/states/current.csv', encoding='utf-8', na_values=None)
    value = DailyUpdate.loc[DailyUpdate['state'].isin(["CT"])]
    value = value[['state', value.columns[2], value.columns[19], value.columns[18], value.columns[26],value.columns[40],
                        value.columns[22],value.columns[23], value.columns[24]]]
    print(value)
    allData = []
    for i in range(value.shape[0]):
        temp = value.iloc[i]
        allData.append(dict(temp))

    historicalData = pd.read_csv('https://data.ct.gov/resource/rf3k-f8fg.csv', encoding='utf-8', na_values=None)
    lineplot = historicalData[['date',historicalData.columns[3],historicalData.columns[4],historicalData.columns[6],historicalData.columns[7],historicalData.columns[8]]].groupby('date').sum().sort_values(by='date')
    lineplot = lineplot.reset_index()
    lineplot['date']= pd.to_datetime(lineplot['date'])
    result = lineplot.groupby([lineplot['date'].dt.year, lineplot['date'].dt.month], as_index=False).agg({'totalcases':sum,'confirmedcases':sum,'totaldeaths':sum,'confirmeddeaths':sum,'hospitalizedcases':sum})
    totalcases=result[result.columns[0]].values.tolist()
    confirmedcases=result[result.columns[1]].values.tolist()
    totaldeaths=result[result.columns[2]].values.tolist()
    confirmeddeaths=result[result.columns[3]].values.tolist()
    hospitalizedcases=result[result.columns[4]].values.tolist()
    print(result)
    newLabels = ["Mar 2020"]
    array_length = len(result)
    for index in range(array_length):
        newLabels[0] == "Mar 2020"
        if index==1: newLabels.append("Apr 2020")
        elif index==2: newLabels.append("May 2020")
        elif index==3: newLabels.append("Jun 2020")
        elif index==4: newLabels.append("Jul 2020")
        elif index==5: newLabels.append("Aug 2020")
        elif index==6: newLabels.append("Sept 2020")
        elif index==7: newLabels.append("Oct 2020")
        elif index==8: newLabels.append("Nov 2020")
        elif index==9: newLabels.append("Dec 2020")
        elif index==10: newLabels.append("Jan 2021")
        elif index==11: newLabels.append("Feb 2021")
        elif index==12: newLabels.append("Mar 2021")
        elif index==13: newLabels.append("Apr 2021")
        elif index==14: newLabels.append("May 2021")
        elif index==15: newLabels.append("Jun 2021")
        elif index==16: newLabels.append("Jul 2021")
        elif index==17: newLabels.append("Aug 2021")
        elif index==18: newLabels.append("Sept 2021")
        elif index==19: newLabels.append("Oct 2021")

    print(newLabels)
    showNursing = 'True'
    context = {'data' : allData, 'showNursing':showNursing, 'newLabels':newLabels, 'totalcases':totalcases, 'confirmedcases':confirmedcases,
               'totaldeaths':totaldeaths,'confirmeddeaths':confirmeddeaths,'hospitalizedcases':hospitalizedcases }
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

def maps(request):
    DailyUpdate = pd.read_csv('https://raw.githubusercontent.com/nytimes/covid-19-data/master/live/us-states.csv',
                              encoding='utf-8', na_values=None)
    value = DailyUpdate.loc[DailyUpdate['state'].isin(["Connecticut"])]
    value = value[['state', value.columns[2], value.columns[3], value.columns[4],
                   value.columns[5], value.columns[6]]]

    allData = []
    for i in range(value.shape[0]):
        temp = value.iloc[i]
        allData.append(dict(temp))
    maps_selection ='True'
    context = {'allData': allData, 'maps': maps_selection}
    return render(request, 'maps.html', context)


def townMap(request):
    Townmap = pd.read_csv('https://data.ct.gov/resource/28fr-iqnx.csv', encoding='utf-8', na_values=None)
    value = Townmap.groupby('town').sum()
    value = value.reset_index()
    value = value[['town', value.columns[2], value.columns[3], value.columns[6]]]

    town = value[value.columns[0]].values.tolist()
    TotalCases = value[value.columns[1]].values.tolist()
    ConfirmedCases = value[value.columns[2]].values.tolist()
    TotalDeaths = value[value.columns[3]].values.tolist()
    townMap ='True'
    context = {'town': town, 'TotalCases': TotalCases, 'ConfirmedCases': ConfirmedCases, 'TotalDeaths': TotalDeaths, 'townMap': townMap}
    return render(request, 'TownMaps.html', context)


def vaccination(request):
    vaccine = pd.read_csv('https://data.ct.gov/resource/pdqi-ds7f.csv', encoding='utf-8', na_values=None)
    vaccine = vaccine.groupby('county').sum()
    vaccine = vaccine.reset_index()
    barplot = vaccine[['county', 'estimated_population', 'first_doses', 'estimated_population_aged_65_to_74',
                       'estimated_population_aged_75_and_above', 'first_doses_administered_age_65_to_74',
                       'first_doses_administered_age_75_and_over']]
    barplot1 = barplot['county'].values.tolist()
    barplot2 = barplot['estimated_population'].values.tolist()
    barplot3 = barplot['first_doses'].values.tolist()
    barplot4 = barplot['estimated_population_aged_65_to_74'].values.tolist()
    barplot5 = barplot['estimated_population_aged_75_and_above'].values.tolist()
    barplot6 = barplot['first_doses_administered_age_65_to_74'].values.tolist()
    barplot7 = barplot['first_doses_administered_age_75_and_over'].values.tolist()

    allData = []
    for i in range(barplot.shape[0]):
        temp = barplot.iloc[i]
        allData.append(dict(temp))
    allData

    vaccination ='True'
    context = {'vaccination': vaccination, 'allData': allData, 'county' :barplot1,  'barplot2' :barplot2, 'barplot3' :barplot3,'barplot4' :barplot4,
               'barplot5': barplot5, 'barplot6' :barplot6, 'barplot7' :barplot7 }
    return render(request, 'vaccinationbyCounty.html', context)


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
    metrics = ['Age','Gender','Ethnicity']
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


    context = {'metrics':metrics, 'selection': selection, 'barplotValMale':barplotValMale, 'barplotValFemale':barplotValFemale,'barplotValOther':barplotValOther,'labels':genderLabels,
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

def schoolCases(request):
    school = pd.read_csv('https://data.ct.gov/resource/ehua-hw73.csv', encoding='utf-8', na_values=None)
    data = school.groupby('date').sum().sort_values(by='date')
    data = data.reset_index()
    data['date'] = pd.to_datetime(data['date'])
    result = data.groupby([data['date'].dt.year, data['date'].dt.month], as_index=False).agg(
        {'staffcases': sum, 'studentcases': sum})
    result

    staffcases = result[result.columns[0]].values.tolist()
    studentcases = result[result.columns[1]].values.tolist()
    newLabels = ["Sept 2020"]
    array_length = len(result)
    for index in range(array_length):
        newLabels[0] == "Sept 2020"
        if index == 1:
            newLabels.append("Oct 2020")
        elif index == 2:
            newLabels.append("Nov 2020")
        elif index == 3:
            newLabels.append("Dec 2020")
        elif index == 4:
            newLabels.append("Jan 2021")
        elif index == 5:
            newLabels.append("Feb 2021")
        elif index == 6:
            newLabels.append("Mar 2021")
        elif index == 7:
            newLabels.append("Apr 2021")
        elif index == 8:
            newLabels.append("May 2021")
        elif index == 9:
            newLabels.append("Jun 2021")
        elif index == 10:
            newLabels.append("Jul 2021")
    schools = 'True'
    fields = ['staffcases', 'studentcases']
    context = { 'staffcases': staffcases, 'newLabels':newLabels, 'studentcases' : studentcases, 'schools': schools}

    return render(request, 'Schools.html', context)

def specimen(request):
    specimen = pd.read_csv('https://data.ct.gov/resource/qfkt-uahj.csv', encoding='utf-8', na_values=None)
    data = specimen.groupby('date').sum().sort_values(by='date')
    data = data.reset_index()
    data['date'] = pd.to_datetime(data['date'])
    result = data.groupby([data['date'].dt.year, data['date'].dt.month], as_index=False).agg(
        {'number_of_pcr_tests': sum, 'number_of_pcr_positives': sum, 'number_of_ag_tests': sum,
         'number_of_ag_positives': sum})
    result

    PCR_Tests = result[result.columns[0]].values.tolist()
    PCR_Positive = result[result.columns[1]].values.tolist()
    AG_Tests = result[result.columns[2]].values.tolist()
    AG_Positive = result[result.columns[3]].values.tolist()

    newLabels = ["Dec 2020"]
    array_length = len(result)
    for index in range(array_length):
        newLabels[0] == "Dec 2020"
        if index == 1:
            newLabels.append("Jan 2021")
        elif index == 2:
            newLabels.append("Feb 2021")
        elif index == 3:
            newLabels.append("Mar 2021")
        elif index == 4:
            newLabels.append("Apr 2021")
        elif index == 5:
            newLabels.append("May 2021")
        elif index == 6:
            newLabels.append("Jun 2021")


    specimenvalue = 'True'

    context = { 'PCR_Tests': PCR_Tests, 'newLabels':newLabels, 'PCR_Positive' : PCR_Positive, 'specimenvalue': specimenvalue, 'AG_Tests': AG_Tests, 'AG_Positive': AG_Positive}

    return render(request, 'specimenCollected.html', context)


def population(request):
    population = pd.read_csv('https://data.ct.gov/resource/hree-nys2.csv', encoding='utf-8', na_values=None)
    data = population.groupby('updatedate').sum().sort_values(by='updatedate')
    data = data.reset_index()
    data['updatedate'] = pd.to_datetime(data['updatedate'])

    test = population.groupby('updatedate').sum().sort_values(by='updatedate')
    test = test.reset_index()

    from datetime import datetime
    listdates = []
    for ts in test['updatedate']:
        listdate = datetime.strftime(pd.to_datetime(ts), format='%m-%d-%Y')
        listdates.append(listdate)
    totalcases = test[test.columns[5]].values.tolist()
    caserate = test[test.columns[6]].values.tolist()
    totaltests = test[test.columns[7]].values.tolist()
    percentpositive = test[test.columns[8]].values.tolist()

    populationvalue = 'True'

    context = { 'totalcases': totalcases, 'caserate':caserate, 'totaltests' : totaltests, 'percentpositive': percentpositive, 'listdates': listdates, 'populationvalue': populationvalue}

    return render(request, '100KPopulation.html', context)





def redirect_view(request):
    response = redirect('/Home-success/')
    return response
