import pandas as games
import quandl
import matplotlib.pyplot as pol
import seaborn as sns
import datetime

games=games.read_csv('ign.csv')
plat_genre=games
games.replace(['Action, Adventure','Action, RPG','Adventure','Fighting',
                 'Platformer','Racing, Action','Racing','Shooter','Simulation']
                ,['Act,adv','Act,RPG','Adv','Fight','Plat','Rac,Act','Race','Shoot','Simltn'],inplace=True)
max_genres=games.groupby('genre')['genre'].count()
new_genres=max_genres.sort_values(ascending=False)[:10]
plat_genre=plat_genre[plat_genre['genre'].isin(new_genres.index)]
plat_genre=plat_genre.groupby(['platform','genre'])['score'].count().reset_index()
plat_genre=plat_genre[plat_genre['score']>10]
plat_genre=plat_genre.pivot('platform','genre','score')
plat_genre=plat_genre.dropna(thresh=8)
sns.heatmap(plat_genre,annot=True,fmt='2.0f',cmap='RdBu_r',linewidths='0.1')
fig=pol.gcf()
fig.set_size_inches(9,9)
pol.yticks(rotation='horizontal')
pol.xticks(rotation='vertical')
pol.show()