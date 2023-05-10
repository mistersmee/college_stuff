# Q1

import pandas as pd
my_lists = [['col1', 'col2'], [2, 4], [1, 3]]
# sets the headers as list
headers = my_lists.pop(0) 
print("Original list of lists:")
print(my_lists)
df = pd.DataFrame(my_lists, columns = headers)
print("New DataFrame")
print(df)

# Q2

import numpy as np

exam_data  = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
        'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
        'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(exam_data , index=labels)
print(df)

# Q3

df1 = pd.DataFrame("people100.csv")
