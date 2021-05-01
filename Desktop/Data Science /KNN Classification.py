from sklearn import datasets
import numpy as np
import pandas as pd
from sklearn import neighbors,metrics
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
#iris=datasets.load_iris()
#x=iris["data"]
#y=iris['target']
#x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)
data=pd.read_csv('/Users/yashjain/Downloads/ART/knnclassifier.data')
x=data[['buying','maint','safety']].values
y=data['class']
Le= LabelEncoder()
for i in range(len(x[0])):
    x[:,i]=Le.fit_transform(x[:,i])
#print x
label_mapping={'unacc':0,'acc':1,'good':2,'vgood':3}
y=y.map(label_mapping)
y=np.asarray(y)
#print y
#model creation
knn=neighbors.KNeighborsClassifier(n_neighbors=25,weights='uniform')
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)
knn.fit(x_train,y_train)
predictions=knn.predict(x_test)
accuracy=metrics.accuracy_score(y_test,predictions)
print ("predictions", predictions)
print ("accuracy", accuracy)
a=323
print ("actual value ",y[a])
print ("predicted value",knn.predict(x)[a])
