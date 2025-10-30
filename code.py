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

# Standard deviation is not an accurate representation of this dataset. You cannot see the standard deviation on the graph because there are the same amount of values as there are rows (217), meaning the standard deviation will be the same.


"""""Anael Edery"""
#Question 4:
sns.lmplot(data = world_data, x = "Life expectancy, female", y ="GNI per capita")
sns.lmplot(data = world_data, x = "Life expectancy, male", y = "GNI per capita")    
    
    
# Question 5:
sns.relplot(data = world_data, x ="Life expectancy, female", y = "Physicians", col = "Region")
sns.relplot(data = world_data, x ="Life expectancy, male", y = "Physicians", col = "Region")