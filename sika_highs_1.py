import csv
from matplotlib import pyplot as plt
from datetime import datetime
file_name="data_analyze\data\sitka_weather_07-2018_simple.csv"
with open(file_name) as f:
    # 打开csv文件
    reader=csv.reader(f)
    # 读取csv文件中的内容
    header_row=next(reader)
    # 读取每一行的抬头名字
    # for column_number,index in enumerate(header_row):
    #     # 获取每一行抬头的名称以及他们的序列
    #     print(column_number,index)
    highs,dates=[],[]
    for row in reader:
        # 遍历每一行
        high=int(row[5])
        # 将第五行的数值赋值给high
        date=datetime.strptime(row[2],'%Y-%m-%d')
        highs.append(high)
        dates.append(date)
    plt.style.use("seaborn")
    fig,ax=plt.subplots(figsize=(20,10))
    fig.autofmt_xdate()
    # 绘制倾斜的日期标签
    ax.set_title("The highest weather of the day",fontsize=24)
    ax.set_xlabel("Date",fontsize=16)
    ax.set_ylabel("tempreture",fontsize=16)
    ax.plot(dates,highs,c='red')
    ax.tick_params(axis="both",which="major",labelsize=14)
    plt.show()