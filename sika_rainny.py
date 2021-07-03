import csv
from matplotlib import pyplot as plt
from datetime import datetime

file_name = "data_analyze\data\sitka_weather_2018_simple.csv"
dead_vally="data_analyze\data\death_valley_2018_simple.csv"
with open(file_name) as f:
    reader=csv.reader(f)
    row_header=next(reader)

    rainny_days,dates=[],[]
    for row in reader:
        rainny_day=float(row[3])
        date=datetime.strptime(row[2],"%Y-%m-%d")
        rainny_days.append(rainny_day)
        dates.append(date)
with open(dead_vally) as vally:
    vally_reader=csv.reader(vally)
try:
    vally_rainny_days,vally_dates=[],[]
    for row in vally_reader:
        vally_rainny_day=row[3]
        vally_date=datetime.strptime(row[2],'%Y-%m-%d')
        vally_rainny_days.append(vally_rainny_day)
        vally_dates.append((vally_date))
except ValueError:
    pass
    fig,ax=plt.subplots()
    plt.style.use("seaborn")
    ax.set_title("Dayily precipitation in Sitka,2018")
    ax.set_xlabel("Date",fontsize=14)
    ax.set_ylabel("ML",fontsize=14)
    ax.plot(dates,rainny_days,c="red",label='Sarika Precipitaion',alpha=0.5,linewidth=3)
    ax.plot(vally_dates,vally_rainny_days,c="blue",label='Vally Precipitaion',alpha=0.5,linewidth=3)
    # ax.fill_between(dates,vally_rainny_days,rainny_days,facecolor="green",alpha=0.5)
    ax.tick_params(axis="both",which="major",labelsize=16)
    plt.ylim((0,5.0))
    # 设置y轴得坐标值
    plt.legend("best")
    plt.show()

