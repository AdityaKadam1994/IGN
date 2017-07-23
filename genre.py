import pandas as raw_data
import quandl
import matplotlib.pyplot as plt
import seaborn as sns
import datetime

raw_data = raw_data.read_csv('ign.csv')
raw_data['genre'].value_counts()[:10].plot(kind='pie',autopct='%1.1f%%',shadow=True,explode=[0.1,0,0,0,0,0,0,0,0,0])
plt.title('Top Genre"s')
plt.show()





