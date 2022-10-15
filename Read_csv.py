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
pd.read_csv('location_of_csv_file//student_results.csv')

#To know where is these files store in your computer system use ‘os’ library
import os
print(os.getcwd())


