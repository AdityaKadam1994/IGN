# Importing pandas
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import accuracy_score

minmax=MinMaxScaler()
# Importing training data set
X_train=pd.read_csv('X_train.csv')
Y_train=pd.read_csv('Y_train.csv')
# Importing testing data set
X_test=pd.read_csv('X_test.csv')
Y_test=pd.read_csv('Y_test.csv')
#Scaling the data 
X_train_minmax=minmax.fit_transform(X_train[['score']])
X_test_minmax=minmax.fit_transform(X_test[['score']])
#print (X_train.head())

#import matplotlib.pyplot as plt
#X_train[X_train.dtypes[(X_train.dtypes=="float64")|(X_train.dtypes=="int64")]
 #                       .index.values].hist(figsize=[11,11])

#plt.show()
knn=KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train[['score']],Y_train.values.ravel())
# Checking the performance of our model on the testing data set
print("accuracy",accuracy_score(Y_test,knn.predict(X_test[['score']]))*100)
    