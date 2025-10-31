# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
""""""Noah Haupt"""

#Part 3:
#Question 1
    # What is the distribution of greenhouse gases across different regions?
    # Is there a positive correlation between International tourism and a country's Gross National Income?
    # Which region has the most amount of countries? Which region has the most amount of subregions? Intermediate Regions?

#Question 2
import pandas as pd
world_data = pd.read_csv("worlddata.csv")

#Question 3
print(world_data.info())
#There are 217 rows in this dataset. Population has 217 non-null values (not empty), meaning it has no empty values for this column because 217-217 = 0. Physicians has 207 non-null values, meaning it has 10 empty values because 217-207 = 10.

#Question 4
print(world_data.nunique())
#The nunique() function provides the number of different, non-null values in each column. For example, Physicians has 207 because 10 of the values are empty, but Region has 5 because there are only 5 different values.

#Question 5
print(world_data.describe())
#The describe() function provides important information for the numerical data only (that's why there's only 12 columns)  such as the count, the mean, the standard deviation, the min and the max, and the first three quartiles (Q1-Q3)

#Question 6
world_data["GNI per capita"] = (world_data["GNI"] / world_data["Population"]).round(2)
gni_per_cap = world_data["GNI per capita"]

#Question 7
#a
print(world_data["Region"].value_counts())
# There are 54 countries in Africa, 50 countries in Asia, 47 countries in Europe, 46 countries in the Americas, and 19 countries in Oceania

#b
print(world_data["High Income Economy"].value_counts())
# There are 67 high income economies.

#Question 8
print(pd.crosstab(world_data["Region"], world_data["High Income Economy"]))
#There are 0 high income economies in Africa, 17 in Americas, 14 in Asia, 31 in Europe, and 4 in Oceania. This answer lines up with the previous question of how many High income countries there are (17+14+31+4 = 67)

#Question 9
women_80 = 0

for x in world_data["Life expectancy, female"]:
    if x > 80:
        women_80 += 1
    else:
        continue
print(women_80)

countries_80 = world_data[world_data["Life expectancy, female"] > 80]

for y in countries_80["Country Name"]:
    print(y,", ", end = '')
#There are 66 countries where female life expectancy is greater than 80. Those countries are: Albania , Australia , Austria , Barbados , Belgium , Bermuda , Canada , Cayman Islands , Channel Islands , Chile , Colombia , Costa Rica , Croatia , Cuba , Curacao , Cyprus , Czech Republic , Denmark , Estonia , Faroe Islands , Finland , France , Germany , Greece , Guam , Hong Kong SAR, China , Iceland , Ireland , Isle of Man , Israel , Italy , Japan , Korea, Rep. , Lebanon , Liechtenstein , Lithuania , Luxembourg , Macao SAR, China , Maldives , Malta , Netherlands , New Caledonia , New Zealand , Norway , Oman , Panama , Poland , Portugal , Puerto Rico , Qatar , San Marino , Singapore , Sint Maarten (Dutch part) , Slovak Republic , Slovenia , Spain , Sri Lanka , St. Martin (French part) , Sweden , Switzerland , Thailand , Turkey , United Kingdom , United States , Uruguay , Virgin Islands (U.S.)


# Part 4
import seaborn as sns
# Question 1: 

world_data["GNI per capita"] = (world_data["GNI"] / world_data["Population"]).round(2)
gni_per_cap = world_data["GNI per capita"]


sns.relplot(data = world_data, x = "Life expectancy, female", y = gni_per_cap)
sns.relplot(data = world_data, x = "Life expectancy, male", y = gni_per_cap)

#Question 2:
sns.relplot(data = world_data, x = "Life expectancy, female", y = gni_per_cap, hue = "Region")
sns.relplot(data = world_data, x = "Life expectancy, male", y = gni_per_cap, hue = "Region")

#Question 3:
sns.relplot(data = world_data, x = "Life expectancy, female", y = gni_per_cap, hue = "Region", kind = "line", errorbar = "sd")
sns.relplot(data = world_data, x = "Life expectancy, male", y = gni_per_cap, hue = "Region", kind = "line", errorbar = "sd")

# Standard deviation is not an accurate representation of this dataset. You cannot see the standard deviation on the graph because the csv file has 217 rows and GNI per capita has 217 unique values. This means that for each row/country, there is only 1 value to show, meaning that there is no variation and therefore no standard deviation will show. 

"""""Anael Edery & Noah Haupt"""
#Question 4:
sns.lmplot(data = world_data, x = "Life expectancy, female", y ="GNI per capita")
sns.lmplot(data = world_data, x = "Life expectancy, male", y = "GNI per capita")    
    
    
# Question 5:
    #1-Is there a correlation between the number of physicians and life expectancy? How does it change in each region? Do wealthier countries have more physicians and longer lives?
sns.relplot(data = world_data, x ="Life expectancy, female", y = "Physicians", col = "Region", hue = "High Income Economy")
sns.relplot(data = world_data, x ="Life expectancy, male", y = "Physicians", col = "Region", hue = "High Income Economy")
    #Interpretation:
        
   #2-Is there a correlation between tertiary education (education after high school) and life expectancy? Does more education lead to a higher life expectancy? Do these values differ between genders? Across regions?
sns.relplot(data = world_data, x ="Tertiary education, female", y = "Life expectancy, female", col = "Region", hue = "Region")
sns.relplot(data = world_data, x ="Tertiary education, male", y = "Life expectancy, male", col = "Region", hue = "Region")
 

   #3-Is there a correlation between population and life expectancy? Do countries with smaller populations have higher life expectancies?
sns.relplot(data = world_data, x ="Life expectancy, female", y = "Population", col = "Region")
sns.relplot(data = world_data, x ="Life expectancy, male", y = "Population", col = "Region")
   
   
   #4-Is there a relationship between tourism and life expectancy? Do regions with more tourists have a high income economy and therefore a higher life expectancy?
sns.relplot(data = world_data, x ="Life expectancy, female", y = "International tourism", col = "Region", hue = "High Income Economy")
sns.relplot(data = world_data, x ="Life expectancy, male", y = "International tourism", col = "Region", hue = "High Income Economy")
   
   #5- Do higher greenhouse gas emissions mean lower life expectancies? Do wealthier countries produce more greenhouse gases?
sns.relplot(data = world_data, x ="Life expectancy, female", y = "International tourism", col = "Region", hue = "High Income Economy", style = "High Income Economy")
sns.relplot(data = world_data, x ="Life expectancy, male", y = "International tourism", col = "Region", hue = "High Income Economy", style = "High Income Economy")


#Question 6
import pandas as pd
world_data = pd.read_csv("worlddata.csv")
import seaborn as sns

world_data["Emissions per capita"] = world_data["Greenhouse gas emissions"] / world_data["Population"]
gases_per_cap = world_data["Emissions per capita"]

#a
sns.relplot(data = world_data, y = "Emissions per capita", x = "Internet use")

#b
emissions_greater = world_data[world_data["Emissions per capita"] > 0.03]

for y in emissions_greater["Country Name"]:
    print(y,", ", end = '')
    
#c,d
sns.relplot(data = world_data, y = "Emissions per capita", x = "Internet use", col = "Region", hue = "High Income Economy", style = "High Income Economy")