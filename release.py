import pandas as new
import quandl
import matplotlib.pyplot as plt
import seaborn as sns
import datetime

new=new.read_csv('ign.csv')
new=new.groupby(['release_year','platform'])['score'].count().reset_index()
new.columns=[['release_year','platform','count']]
new=new.sort_values(by='count',ascending=False)
new=new.drop_duplicates(subset=['release_year'],keep='first')
new=new.sort_values(by='release_year')
new.set_index('release_year',inplace=True)
new.plot.barh(color='#ff0000',width=0.9)
fig=plt.gcf()
fig.set_size_inches(10,10)
for i, p in enumerate(zip(new.platform, new['count'])):
    plt.text(s=p,x=1,y=i,fontweight='bold',color='white')
plt.show()

analysis= "After seeing the graph we can clearly say that most no of games were release in 2008.Most os the games were released on Wii platform"
print (analysis)