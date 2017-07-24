import pandas as games
import quandl
import matplotlib.pyplot as pol
import seaborn as sns
import datetime
fig,ax=pol.subplots(1,2,figsize=(18,10))
games=games.read_csv('ign.csv')
sns.countplot(games['release_month'],ax=ax[0],palette='Set1').set_title('Releases On Months')
pol.ylabel('')
sns.countplot(games['release_year'],ax=ax[1],palette='Set1').set_title('Releases on Years')
pol.xticks(rotation=90)
pol.show()