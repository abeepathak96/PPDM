# This is a python file used for the data cleaning of the adult dataset # 

# imports # 
import pandas as pd 
import sklearn 
import urllib2
from urllib2 import urlopen 



# getting the dataset 

adult_set = "https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data"
url = urlopen(adult_set) 

# loading the dataset

dataset = pd.read_csv(url)
dataset.columns = ['Age', 'Workclass', 'Salary', 'Education', 'Education_number', 'Marital_satus', 'Occupation', 'Relationship', 'Race', 'Sex', 'Capital_gain', 'Capital_loss', 'Hours_per_week', 'Native_country', 'Generalize']

# dataset shape # 

print(dataset.shape)

# describe of the dataset #

print(dataset.describe())

# check for the null value # 

dataset.isnull().any()

