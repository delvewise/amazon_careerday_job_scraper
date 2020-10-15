# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 08:50:27 2020

@author: nickd
"""
# Importing the libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns
plt.style.use('ggplot')
import re
# Importing the dataset 
df = pd.read_csv('C:/Users/nickd/OneDrive/Desktop/delve/CareerDaySept15clean.csv')

df.info()


#clean up job id
df['job_id']
df['job_id']= df['job_id'].str.split(': ', 1).str[1] 
df['job_id']
#clean Job title
df['job_title']
df['job_title']= df['job_title'].str.split("'", 2).str[1]
df['job_title']

#clean description and Qual by converting to string?
df['job_description']

df['job_description'] = df['job_description'].str.split("[", 1).str[1]
df['job_description'] = df['job_description'].str.split("]", 1).str[0]
df['job_description'][0]

#check datatype of columns; this case we have objects
df['job_location'].dtype
#convert the value objects into lists for value extraction
df['job_location']= df['job_location'].to_numpy()
# Renames if needed
#df = df.rename(columns={'Minimum Qualifications': 'Minimum_Qualifications'})

#cleaning text
#https://www.analyticsvidhya.com/blog/2020/06/nlp-project-information-extraction/
# function to preprocess speech
#def clean(text):
    
    # removing new line characters
#    text = re.sub('\n ','',str(text))
#    text = re.sub('\n',' ',str(text))
#    # removing apostrophes
#    text = re.sub("'s",'',str(text))
#    # removing hyphens
#    text = re.sub("-",' ',str(text))
#    text = re.sub("— ",'',str(text))
#    # removing quotation marks
#    text = re.sub('\"','',str(text))
#    # removing salutations
#    text = re.sub("Mr\.",'Mr',str(text))
#    text = re.sub("Mrs\.",'Mrs',str(text))
#    # removing any reference to outside text
#    text = re.sub("[\(\[].*?[\)\]]", "", str(text))
#    
#    return text

# preprocessing speeches
df['Speech_clean'] = df['Speech'].apply(clean)

# Taking care of missing data get a NONE/NA 
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
imputer.fit(X[:, 1:3])
X[:, 1:3] = imputer.transform(X[:, 1:3])
print(X)

# Encoding categorical data
# Encoding the Independent Variable
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [0])], remainder='passthrough')
X = np.array(ct.fit_transform(X))
print(X)
# Encoding the Dependent Variable
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
y = le.fit_transform(y)
print(y)

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 1)
print(X_train)
print(X_test)
print(y_train)
print(y_test)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train[:, 3:] = sc.fit_transform(X_train[:, 3:])
X_test[:, 3:] = sc.transform(X_test[:, 3:])
print(X_train)
print(X_test)