import pandas as games
import quandl
import matplotlib.pyplot as plt
import seaborn as sns
import datetime

games=games.read_csv('ign.csv')
games['score_phrase']=games['score_phrase'].map({'Awful':'Flop','Bad':'Flop','Disaster':'Flop','Unbearable':'Flop','Painful':'Flop','Mediocre':'Good','Okay':'Good','Great':'Hit','Amazing':'Hit','Masterpiece':'Masterpiece','Good':'Good'})
games=games[['score_phrase','platform','genre','score']]
max_platforms=games['platform'].value_counts().index[:15]
plat=games[games['platform'].isin(max_platforms)]
plat=plat.groupby(['platform','score_phrase'])['score'].count().reset_index()
plat=plat.pivot('platform','score_phrase','score')
plat.plot.barh(width=0.9)
fig=plt.gcf()
fig.set_size_inches(12,14)
plt.show()