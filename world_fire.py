import pandas as pd
import plotly.express as ps
import csv
from datetime import datetime,time
fire_file="data_analyze\data\world_fires_1_day.csv"

with open(fire_file) as fire:
    fire_reader = csv.reader(fire)
    row_head=next(fire_reader)

    brightness,lons,lats,dates,times=[],[],[],[],[]
    for row in fire_reader:
        bright=float(row[2])
        lon=row[1]
        lat=row[0]
        fire_date=datetime.strptime(row[5],'%Y-%m-%d')
        fire_time=((row[6][0:2]),row[6][2:5])
        brightness.append(bright)
        lons.append(lon)
        lats.append(lat)
        dates.append(fire_date)
        times.append(fire_time)
    data=pd.DataFrame(zip(brightness,lons,lats,dates,times),columns=["Fire strongest","经度","维度","日期","时间"])
    data.head()

    fig=ps.scatter(
        data,
        x='经度',
        y='维度',
        title="全球火灾强度",
        # hover_data=f'{dates}\n{times}',
        color="Fire strongest",
        size="Fire strongest",
        size_max=10,
        labels={"x":"经度","y":"维度"},
        hover_name='日期'
    )

fig.write_html("World_Fire.html")
fig.show()