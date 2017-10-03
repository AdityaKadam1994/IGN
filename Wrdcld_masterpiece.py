import pandas as pd
import quandl
import matplotlib.pyplot as plt
import seaborn as sns
import datetime
from wordcloud import WordCloud, STOPWORDS

pd=pd.read_csv('ign.csv')
pd=pd[pd['score_phrase']=='Masterpiece']
plt.subplots(figsize=(10,10))
wordcloud = WordCloud(
                          stopwords=STOPWORDS,
                          background_color='white',
                          width=1200,
                          height=1000
                         ).generate(" ".join(pd['title']))


plt.imshow(wordcloud)
plt.axis('off')
plt.show()