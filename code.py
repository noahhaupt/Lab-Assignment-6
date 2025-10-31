# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
""""""Noah Haupt"""

import pandas as pd
import seaborn as sns

world_data = pd.read_csv("worlddata.csv")

# Part 4
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
    #Interpretation:
 

   #3-Is there a correlation between population and life expectancy? Do countries with smaller populations have higher life expectancies?
   
   
   #Interpretation:
   
   
   #4-Is there a relationship between tourism and life expectancy? Do regions with more tourists have less life expectancy rates?
 
   #Interpretation:
   
   #5- 
   
   #Interpretation: