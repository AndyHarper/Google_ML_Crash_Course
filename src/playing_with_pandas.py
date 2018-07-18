'''
Created on 29 May 2018

@author: andrew.harper
'''
import pandas as pd
print(pd.__version__)

#A series is just a column
#A DataFrame is a relational table with rows and named columns. One or more series with names


DataFrameObject1 = pd.Series(['San Francisco', 'San Jose', 'Sacramento'])
print(DataFrameObject1)

city_names = pd.Series(['San Francisco', 'San Jose', 'Sacramento'])
population = pd.Series([852469, 1015785, 485199])

#to create a dataframe from a series you give each series a name
pd.DataFrame({ 'City name': city_names, 'Population': population })

#you can load whole datasets into DataFrames like:
california_housing_dataframe = pd.read_csv("https://storage.googleapis.com/mledu-datasets/california_housing_train.csv", sep=",")
interesting_stats_on_dataframe = california_housing_dataframe.describe()
print(interesting_stats_on_dataframe)

#It can be indexed like this:
print(california_housing_dataframe[0:3])

#another way to print the first few records is:
print(california_housing_dataframe.head()) #first 5 in this case

#ACCESSING DATA
cities = pd.DataFrame({ 'City name': city_names, 'Population': population }) #name and population
print(cities) 
print(type(cities['City name'])) #tells you that City name is a pandas series
print(cities['City name'])
print(type(cities)) #tells you that cities is a dataframe? yes :)

#you can access each name of the cities
print(type(cities['City name'][1])) #tells you its a string
print(cities['City name'][1]) #gives the second city

thousand_people = population/1000 #you can manipulate series like arrays in matlab
import numpy as np
log_population = np.log(population) #even take logs

populations_dataframe = pd.DataFrame({'Population': population,'Log Population': log_population}) #made a new dataframe from population info

#you can query:
check1 = population.apply(lambda val: val > 1000000)
print(check1.head())

#you can add data to a dataframe as a new series:
cities['Area square miles'] = pd.Series([46.87, 176.53, 97.92])
cities['Population density'] = cities['Population'] / cities['Area square miles'] #and create new series based on calculated data

print(cities.head())