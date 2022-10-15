#Pandas Read CSV File in Python
#What is CSV File
#A CSV is a comma separated values file which allows to store data in tabular format. 
#That data includes numbers and text in plain text form. CSV is an extension of any file or spreadsheet .
#Advantages of CSV File
#1. Universally used
#2. Easy to read
#3. Easy to understand
#4. Quick to create

#How to Read or Import CSV File in Python IDLE or IDE

import pandas as pd
df= pd.read_csv('location_of_csv_file//student_results.csv')

#To know where is these files store in your computer system use ‘os’ library
import os
print(os.getcwd())

#To know the type of the dataset use type function	
type(df)

#To know all the columns name
df.columns

#If you want to read some specific rows of the dataset use nrows parameters#
df = pd.read_csv('location//Fortune_10.csv', nrows = 1)

df = pd.read_csv('location//Fortune_10.csv', nrows = 5)

#If you want to read some specific columns of the dataset use nrows parameters#
df = pd.read_csv('location\\Fortune_10.csv', usecols = [0])  # [index]
df = pd.read_csv('location\\Fortune_10.csv', usecols = [0,1])  # [index]

#If you want to skip row#
df = pd.read_csv('location\\Fortune_10.csv', skiprows = 1)

#If you want to take any column in index#
df = pd.read_csv('location\\Fortune_10.csv', index_col = 'ID') # index_col = 'column name' 
df = pd.read_csv('location\\Fortune_10.csv', index_col = 0) #or index value







