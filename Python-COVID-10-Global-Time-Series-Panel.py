
# Import packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 
sns.set()


# load the data of race, age, sex, proverty
# The data is from NYC health department 

race=pd.read_csv('https://raw.githubusercontent.com/nychealth/coronavirus-data/master/by-race.csv')
age=pd.read_csv('https://raw.githubusercontent.com/nychealth/coronavirus-data/master/by-age.csv')
sex=pd.read_csv('https://raw.githubusercontent.com/nychealth/coronavirus-data/master/by-sex.csv')
poverty=pd.read_csv('https://raw.githubusercontent.com/nychealth/coronavirus-data/master/by-poverty.csv')

# Race: Plot confirmed cases and death by Race Group
plt.figure(figsize=(20,5))
plt.subplot(1,2,1)
sns.barplot(race.RACE_GROUP, race.CASE_COUNT)
plt.title("Confirmed Cases by Race Group in NYC", fontsize=20)

plt.subplot(1,2,2)
sns.barplot(race.RACE_GROUP, race.DEATH_COUNT)
plt.title("Death by Race Group in NYC", contsize=20)
plt.show()

# Age: Plot the covid-19 confiremd cases and death in different age layers
plt.figure(figsize=(20,5))
plt.subplot(1,2,1)
sns.barplot(age.iloc[:-1].AGE_GROUP,age.iloc[:-1].CASE_COUNT)
plt.title('Confirmed Cases by Age in NYC',fontsize=20)

plt.subplot(1,2,2)
sns.barplot(age.iloc[:-1].AGE_GROUP,age.iloc[:-1].DEATH_COUNT)
plt.title('Death by Age in NYC',fontsize=20)
plt.show()

# Sex: Plot the COVID-19 confirmed cases and death in different genders
plt.figure(figsize=(20,5))
plt.subplot(1,2,1)
sns.barplot(sex.iloc[:-1].SEX_GROUP, sex.iloc[:-1].CASE_COUNT)
plt.title("Confirmed Cases by Gender in NYC", fontsize=20)

plt.subplot(1,2,2)
sns.barplot(sex.iloc[:-1].SEX_GROUP, sex.iloc[:-1].DEATH_COUNT)
plt.title("Death by Gender in NYC", fontsize=20)
plt.show()

# Plot the covid-19 confiremd cases and death in different poverty level
plt.figure(figsize=(20,5))
plt.subplot(1,2,1)
sns.barplot(poverty.POVERTY_GROUP,poverty.CASE_COUNT)
plt.title('Confirmed Cases by Poverty Level in NYC',fontsize=20)
plt.subplot(1,2,2)
sns.barplot(poverty.POVERTY_GROUP,poverty.DEATH_COUNT)
plt.title('Death by Poverty Level in NYC',fontsize=20)
plt.show()

# Borough
# load the data 
url='https://raw.githubusercontent.com/nychealth/coronavirus-data/master/deaths/deaths-by-boro-age.csv'
borough=pd.read_csv(url)
print(borough)

# Borough
# Plot the covid-19 confiremd cases and death in different borough
plt.figure(figsize=(20,20))
for i in range(len(borough)):
    plt.subplot(3,2,i+1)
    sns.barplot(borough.columns[1:],borough.iloc[i][1:])
    plt.title('Number of Death in {}'.format(borough.iloc[i][0]),fontsize=20)
plt.show()

# Trend of confirmed cases and death
url1='https://raw.githubusercontent.com/nychealth/coronavirus-data/master/case-hosp-death.csv'
nyc_data = pd.read_csv(url1)

# Convert NYC['DATE_OF_INTEREST'] column into datetime type
nyc['DATE_OF_INTEREST'] = pd.to_datatime(nyc['DATE_OF_INTEREST'])

# Plot the linegraph for the trend of confirmed cases hospitalised count and death count from May to Jun 2020
plt.figure(figsize=(10,5))
plt.plot('DATE_OF_INTEREST', 'CASE_COUNT', data=nyc_data='CASE_COUNT'.title())
plt.plot('DATE_OF_INTEREST', 'HOSPITALISED_COUNT', data=nyc_data, label='HOSPITALISED COUNT'.title())
plt.plot('DATE_OF_INTEREST', 'DEATH_COUNT', data=nyc_data, label='DEATH_COUNT'.title())
plt.title("COVID-19 in NYC", fontsize=20)
plt.legend()




