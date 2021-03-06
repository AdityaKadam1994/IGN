import pandas as pd
import quandl
import matplotlib.pyplot as pol
import seaborn as sns
import datetime

pd = pd.read_csv('ign.csv')
pd['score_phrase'].value_counts()[:8].plot(kind='pie',autopct='%1.1f%%',shadow=True,explode=[0.1,0,0,0,0,0,0,0])
pol.title('Popular Platforms')
pol.show()
