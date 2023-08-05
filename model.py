from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import pickle
import pandas as pd


df=pd.read_csv(r"iris.csv")
df=pd.DataFrame(df)


X=df.iloc[:,:-1]


y=df['Class']

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,
                                               random_state=50)


sc=StandardScaler()

X_train=sc.fit_transform(X_train)
X_test=sc.transform(X_test)


classifier=RandomForestClassifier()
classifier.fit(X_train,y_train)

pickle.dump(classifier, open('model.pkl',"wb"))