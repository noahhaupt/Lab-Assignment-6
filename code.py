# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
""""""Noah Haupt"""

import pandas as pd
import seaborn as sns

world_data = pd.read_csv("Lab-Assignment-6/worlddata.csv")

# Part 4
# Question 1: 

world_data["GNI per capita"] = world_data["GNI"] / world_data["Population"]
gni_per_cap = round(world_data["GNI per capita"],2)
sns.relplot(data = world_data, x = "Life expectancy, female", y = gni_per_cap)
sns.relplot(data = world_data, x = "Life expectancy, male", y = gni_per_cap)

#Question 2:
sns.relplot(data = world_data, x = "Life expectancy, female", y = gni_per_cap, hue = "Region")
sns.relplot(data = world_data, x = "Life expectancy, male", y = gni_per_cap, hue = "Region")

#Question 3:
sns.relplot(data = world_data, x = "Life expectancy, female", y = gni_per_cap, hue = "Region", kind = "line", errorbar = "sd")
sns.relplot(data = world_data, x = "Life expectancy, male", y = gni_per_cap, hue = "Region", kind = "line", errorbar = "sd")