import csv
from matplotlib import pyplot as plt
from datetime import datetime

file_name = "data_analyze\data\sitka_weather_2018_simple.csv"
with open(file_name) as f:
    reader = csv.reader(f)
    header_row=next(reader)
    dates,highs,lows=[],[],[]
    for row in reader:
        date=datetime.strptime(row[2],'%Y-%m-%d')
        dates.append(date)
        high=int(row[5])
        highs.append(high)
        low=int(row[6])
        lows.append(low)
    
    fig,ax=plt.subplots()
    plt.style.use("seaborn")
    ax.set_title("The day's temperture different in July,2018",fontsize=24)
    ax.set_xlabel("date",fontsize=14)
    ax.set_ylabel("tempreture",fontsize=14)
    ax.plot(dates,highs,c="red",alpha=0.5,label='high')
    ax.plot(dates,lows,c="blue",alpha=0.5,label='low')
    ax.fill_between(dates,highs,lows,facecolor='green',alpha=0.8)
    ax.tick_params(axis='both',which='major',labelsize=16)
    plt.legend(loc='best')
    plt.show()