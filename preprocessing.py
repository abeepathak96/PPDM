# imports #

import pandas as pd 
import numpy 
import urllib2
from urllib2 import urlopen
from pandas.tools.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import preprocessing


# assigning a variable of lable encoding # 
le = preprocessing.LabelEncoder()
# loading the dataset and attributes names into the dataset #
dataset = pd.read_csv('adult.data.txt', header = None)
dataset.columns = ['Age', 'Workclass', 'Salary', 'Education', 'Education_number', 'Marital_status', 'Occupation', 'Relationship', 'Race', 'Sex', 'Capital_gain', 'Capital_loss', 'Hours_per_week', 'Native_country', 'Generalize'] 

# print shape of the dataset 
print(dataset.shape)

# description of the dataset
#print(dataset.describe ())

# check if there is any null value #
dataset.isnull().any()

# see the data types of the rows in the dataset #
#print(dataset.dtypes)

# select the rows having object data type from the dataset # 
object_dataset = dataset.select_dtypes(include=['object'])
#print(object_dataset.head())

# converting the counting columns into the numbers # 
#object_dataset.value_counts()

#dataset.plot (kind='box', subplots=True, layout=(6,6), sharex=False, sharey=False)
#plt.show ()

# histograms
#dataset.hist ()
#plt.show ()

# scatter plot matrix
#scatter_matrix (dataset)
#plt.show ()	

# lable encode workclass columnn #
le.fit(['1','2','3','4','5','6','7','8'])
dataset['workclass_encoded'] = le.fit_transform(dataset['Workclass'])

# lable encode education column #
dataset['education_encoded'] = le.fit_transform(dataset['Education'])

# lable marital status column #
dataset['marital-status_encoded'] = le.fit_transform(dataset['Marital_status'])

print(dataset.head(30))