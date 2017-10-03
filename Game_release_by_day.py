import pandas as pd
import quandl
import matplotlib.pyplot as pol
import seaborn as sns
import datetime

pd = pd.read_csv('ign.csv')
pd.groupby('release_day')['genre'].count().plot(color='y')
pol.title('Release By day')
pol.grid()
pol.show()





