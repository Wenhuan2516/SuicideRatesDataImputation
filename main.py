import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import dask.dataframe as ddf
from pandas import Series, DataFrame
import seaborn as sn
import plotly.express as px

county_adjacency = pd.read_csv('county_adjacency.txt', sep='\t', dtype = {'01001': object, '01001.1': 'object'})
county_adjacency = county_adjacency.rename(columns = {'Autauga County, AL': 'county', '01001': 'fips',  'Autauga County, AL.1': 'Neighbors', '01001.1':'Neighbor Code'})
list1 = county_adjacency['county'].tolist()

countyList = []
for i in range(len(list1)):
    if pd.isna(list1[i]) == False:
        countyList.append(i)

for i in range(len(countyList)-1):
    k = countyList[i+1] - countyList[i] -1
    for j in range(k):
        list1[countyList[i]+j+1] = list1[countyList[i]]

list2 = county_adjacency['fips'].tolist()
for i in range(len(countyList)-1):
    k = countyList[i+1] - countyList[i] -1
    for j in range(k):
        list2[countyList[i]+j+1] = list2[countyList[i]]

list3 = county_adjacency['Neighbors'].tolist()
list4 = county_adjacency['Neighbor Code'].tolist()

data={'county': list1, 'fips': list2, 'Neighbors': list3, 'Neighbor Code': list4}
df_new =pd.DataFrame(data)

def str_cat(x):
    return x.str.cat(sep=', ')

df_new = df_new.groupby(['county', 'fips']).agg({'Neighbors': str_cat, 'Neighbor Code': str_cat})
df_new = df_new.reset_index()

df_sd_15 = pd.read_csv(r'Suicide_new/suicide_2015.txt', sep='\t',dtype={"County Code": str})
df_sd_15 = df_sd_15.drop("Notes",1)
df_sd_15 = df_sd_15.dropna(how = 'any')
df_sd_15['Deaths']=df_sd_15['Deaths'].astype(int)
df_sd_15['Population']=df_sd_15['Population'].astype(int)
df_sd_15['SuicideDeathRate'] = (df_sd_15['Deaths'] / df_sd_15['Population'])*100000

df_sd_15 = df_sd_15.rename(columns = {'County Code': 'fips', 'County': 'county'})
df_sd_15 = df_sd_15[['county', 'fips', 'SuicideDeathRate']]
df_final = df_new.merge(df_sd_15, on = ['county','fips'] , how = 'left')


list_suicide = df_final['SuicideDeathRate'].tolist()
fipsList = df_final['fips'].tolist()
dict1 = {}
for i, j in zip(fipsList, list_suicide):
    dict1[i] = j

def findMissingSuicideRate(suicide, fips, neighbor):
    if pd.isna(suicide) == True:
        neighborList = neighbor.split(', ')
        rateSum = 0
        k = 0
        for code in neighborList:
            if code in dict1:
                if pd.isna(dict1[code]) == False:
                    k = k + 1
                    rateSum = rateSum + dict1[code]
        if k != 0:
            mean_rate = rateSum/k
            return mean_rate
    else:
        return suicide

df_final['SuicideDeathRate'] = df_final.apply(lambda x: findMissingSuicideRate(x['SuicideDeathRate'], x['fips'], x['Neighbor Code']), axis = 1)

list_suicide2 = df_final['SuicideDeathRate'].tolist()
list_fips = df_final['fips'].tolist()
dict2 = {}
for i, j in zip(list_fips, list_suicide2):
    dict2[i] = j

def findMissingSuicideRate2(suicide, fips, neighbor):
    if pd.isna(suicide) == True:
        neighborList = neighbor.split(', ')
        rateSum = 0
        k = 0
        for code in neighborList:
            if code in dict2:
                if pd.isna(dict2[code]) == False:
                    k = k + 1
                    rateSum = rateSum + dict2[code]
        if k != 0:
            mean_rate = rateSum/k
            return mean_rate
    else:
        return suicide

df_final['SuicideDeathRate'] = df_final.apply(lambda x: findMissingSuicideRate2(x['SuicideDeathRate'], x['fips'], x['Neighbor Code']), axis = 1)


list_suicide3 = df_final['SuicideDeathRate'].tolist()
list_fips = df_final['fips'].tolist()
dict3 = {}
for i, j in zip(list_fips, list_suicide3):
    dict3[i] = j

def findMissingSuicideRate3(suicide, fips, neighbor):
    if pd.isna(suicide) == True:
        neighborList = neighbor.split(', ')
        rateSum = 0
        k = 0
        for code in neighborList:
            if code in dict3:
                if pd.isna(dict3[code]) == False:
                    k = k + 1
                    rateSum = rateSum + dict3[code]
        if k != 0:
            mean_rate = rateSum/k
            return mean_rate
    else:
        return suicide


df_final['SuicideDeathRate'] = df_final.apply(lambda x: findMissingSuicideRate3(x['SuicideDeathRate'], x['fips'], x['Neighbor Code']), axis = 1)

list_suicide4 = df_final['SuicideDeathRate'].tolist()
list_fips = df_final['fips'].tolist()
dict4 = {}
for i, j in zip(list_fips, list_suicide4):
    dict4[i] = j

def findMissingSuicideRate4(suicide, fips, neighbor):
    if pd.isna(suicide) == True:
        neighborList = neighbor.split(', ')
        rateSum = 0
        k = 0
        for code in neighborList:
            if code in dict4:
                if pd.isna(dict4[code]) == False:
                    k = k + 1
                    rateSum = rateSum + dict4[code]
        if k != 0:
            mean_rate = rateSum/k
            return mean_rate
    else:
        return suicide

df_final['SuicideDeathRate'] = df_final.apply(lambda x: findMissingSuicideRate4(x['SuicideDeathRate'], x['fips'], x['Neighbor Code']), axis = 1)

df_missing = df_final[pd.isna(df_final['SuicideDeathRate']) == True]
df_final.shape[0] - df_missing.shape[0]
df_final2 = df_final[['county', 'fips', 'SuicideDeathRate']]
df_final2.to_csv('SuicideRate_Imputed_2015.csv')

def defineRange(value):
    if value == 0:
        return 'No data'
    elif value > 0 and value <= 10:
        return '<= 10'
    elif value >= 10.1 and value <= 12:
        return '10.1-12'
    elif value >= 12.1 and value <= 14:
        return '12.1-14'
    elif value >= 14.1 and value <= 16:
        return '14.1-16'
    elif value >= 16.1 and value <= 18:
        return '16.1-18'
    elif value >= 18.1 and value < 20:
        return '18.1-20'
    elif value >= 20.1 and value <= 22:
        return '20.1-22'
    elif value >= 22.1 and value < 24:
        return '22.1-24'
    elif value >= 24.1 and value <= 28:
        return '24.1-28'
    elif value >= 28.1 and value < 36:
        return '28.1-36'
    else:
        return '>36'

df_final['SuicideRateRange'] = df_final['SuicideDeathRate'].apply(defineRange)
df_final = df_final.sort_values("SuicideDeathRate", axis = 0, ascending = False)
color_map = {'No data': '#D1D0CE', '<=10': '#00008b', '10.1-12': '#4997d0', '12.1-14': '#00cc99', '14.1-16': '#ace1af', '16.1-18': '#fff8dc',
            '18.1-20': '#ffff99', '20.1-22': '#ffef00', '22.1-24': '#ffa700', '24.1-28': '#e34234', '28.1-36': '#dc143c', '>36': '#990000'}
from urllib.request import urlopen
import json
with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)

import pandas as pd
import plotly.express as px

fig = px.choropleth_mapbox(df_final, geojson=counties, locations='fips', color='SuicideRateRange',
                           color_discrete_map = color_map,
                           mapbox_style = 'carto-positron',
                           zoom = 3, center = {"lat": 37.0902, "lon": -95.7129}
                          )
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()



