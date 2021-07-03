import plotly
import requests
from plotly import offline
from plotly.graph_objects import Bar
url='https://api.github.com/search/repositories?q=language:python&sort=stars'
headers={'Accept':'application/vnd.github.v3+json'}
r=requests.get(url,headers=headers)
print(f'Status code:{r.status_code}')
# 将API响应赋给一个变量
response_dict=r.json()

repo_links,stars,labels=[],[],[]
for repo_dict in response_dict['items']:
    repo_name=(repo_dict['name'])
    repo_url=repo_dict['html_url']
    repo_link=f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)
    stars.append(repo_dict['stargazers_count'])

    owner=repo_dict['owner']['login']
    description=repo_dict['description']
    label=f'{owner}<br/>{description}'
    labels.append(label)
data=[
    {'type' : 'bar',
    'x':repo_links,
    'y':stars,
    'hovertext':labels,
    'marker':{
        'color':'rgb(60,100,150)',
        "line":{'width':1.5,'color':'rgb(25,25,25)'}
    },
    'opacity':0.6,
    # 图表的不透明度
    }
]

x_axis_config={'title':'Repository','titlefont':{'size':24},'tickfont':{'size':14}}
y_axis_config={'title':'Stars','titlefont':{'size':24},'tickfont':{'size':14},}
my_layout={
    'title':'Github 上最受欢迎的python仓库',
    'titlefont':{'size':28},
    'xaxis':x_axis_config,
    'yaxis':y_axis_config
}

offline.plot({'data':data,'layout':my_layout},filename="最受欢迎的python.html")