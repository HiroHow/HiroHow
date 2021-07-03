import json
import plotly.express as px
# plotly.express 功能和matplotlib
import pandas as pd
from matplotlib import pyplot as plt
earth_quake_data='data_analyze\\data\\eq_data_30_day_m1.json'

with open(earth_quake_data) as eq:
    all_eq_data=json.load(eq)

all_eq_dicts=all_eq_data['features']
# 将json特定字典里的值赋值
my_layout=all_eq_data['metadata']['title']
mags,titles,lons,lats=[],[],[],[]
for eq_dict in all_eq_dicts:
    # mag=eq_dict['properties']['mag']
    # # 去properties底下的mag赋值给mag
    # title=eq_dict['properties']['title']
    # lon=eq_dict['geometry']['coordinates'][0]
    # lat=eq_dict['geometry']['coordinates'][1]
    # 同上
    mags.append(eq_dict['properties']['mag'])
    titles.append(eq_dict['properties']['title'])
    lons.append(eq_dict['geometry']['coordinates'][0])
    lats.append(eq_dict['geometry']['coordinates'][1])

data=pd.DataFrame(
    data=zip(lons,lats,titles,mags),columns=['经度','维度','位置','震级']
)
# 用pandas打包数据，创建图表
data.head()

fig=px.scatter(
    data,
    x=lons,
    y=lats,
    labels={'x':'经度','y':'维度'},
    range_x=[-200,200],
    range_y=[-90,90],
    width=800,
    height=800,
    title=my_layout,
    size='震级',
    # 将大小设为震级，震级越大，点越大
    size_max=10,
    color='震级',
    # 渐变，越大越深
    hover_name='位置'
)

fig.write_html('global_earthquakes.html')
fig.show()
# fig,ax=plt.subplots()
