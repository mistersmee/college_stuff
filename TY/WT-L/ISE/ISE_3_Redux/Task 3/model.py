# Importing the libraries
import numpy as np
import pandas as pd
import pickle

df = pd.read_csv('Social_Net_class.csv')

x = df[['Age', 'EstimatedSalary']].values
y = df['Purchased'].values

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 45)

from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier(max_depth = 6, random_state = 45)
model.fit(x_train, y_train)

# Saving model to disk
pickle.dump(model, open('model.pkl','wb'))

# Loading model to compare the results
model2 = pickle.load(open('model.pkl','rb'))

print(model.predict([['50', '50000']]))
