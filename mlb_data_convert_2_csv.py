from pybaseball import statcast
import pandas as pd
import numpy as np
import csv

list_months = ['05', '06', '07', '08', '09']
list_years = ['21', '22']

list_dfs = []

for year in list_years:
    for month in list_months[0:-1]:
        start = '20' + year + '-' + month + '-01'
        end = '20' + year + '-' + list_months[list_months.index(month) + 1] + '-01'
        data = statcast(start_dt = start, end_dt = end)
        list_dfs.append(data)

final_df = pd.concat(list_dfs)
final_df = final_df.drop_duplicates()
final_df.to_csv('pybaseballdf.csv')



