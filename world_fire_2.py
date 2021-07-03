import csv
import plotly.express as ps
import pandas as pd
from datetime import datetime

fire_file="data_analyze\data\world_fires_7_day.csv"
with open(fire_file) as fire_f:
    fire_reader = csv.reader(fire_f)
    head_row = next(fire_reader)

    for column_number, index in enumerate(head_row):
        print(column_number,index)

    lats,lons,brights,fire_dates,fire_times=[],[],[],[],[]
    for row in fire_reader:
        lats.append(row[0])
        lons.append(row[1])
        brights.append(row[2])
        fire_date=datetime.strptime(row[5],'%Y-%m-%d')
        # fire_dates.append(fire_date)
        # fire_times.append(row[6][0:2]+','+row[6][3:5])
    print(lats)

    data = pd.DataFrame([])