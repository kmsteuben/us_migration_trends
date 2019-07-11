# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 15:51:07 2019

@author: steuben
"""
import requests
import pandas as pd

years = list(range(2005, 2018))

# Download data from u.s. census website
for year in years:
    print(year)
    url = "https://www2.census.gov/programs-surveys/demo/tables/geographic-mobility/2017/state-to-state-migration/State_to_State_Migrations_Table_" + str(year) + ".xls"
    print(url)
 
    r = requests.get(url)
 
    with open("//ihme.washington.edu/IHME/HOMES/steuben/repos/us_migration_flows/data/raw_data_" + str(year) + ".xls", "wb") as code:
        code.write(r.content)
        
# clean xls    
        
# the first 4 rows of xls are unneeded so read in after that row
data = pd.read_excel('//ihme.washington.edu/IHME/HOMES/steuben/repos/us_migration_flows/data/raw_data_2017.xls', skiprows = 5)

#drop rwos where everything is NaN
data.dropna(axis = 0, how = 'all')

# delete repeated "current residence" columns
drop_cols = ['Current residence in --.' + str(x) for x in range(1,12)]
data = data.drop(drop_cols, axis = 1)
data.iloc[0]