import pandas as year08
import quandl
import matplotlib.pyplot as plt
import seaborn as sns
import datetime
from wordcloud import WordCloud, STOPWORDS

year08=year08.read_csv('ign.csv')
year08=year08[year08['release_year']==2008]
plt.subplots(figsize=(10,10))
wordcloud = WordCloud(
                          stopwords=STOPWORDS,
                          background_color='white',
                          width=1200,
                          height=1000
                         ).generate(" ".join(year08['title']))


plt.imshow(wordcloud)
plt.axis('off')
plt.show()