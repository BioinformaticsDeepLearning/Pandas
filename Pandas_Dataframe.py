###############################################################################################################################
#DataFrame:  2-D, size-mutable, hetergenous tabular data structure wit labeled axes (rows, columns)
###############################################################################################################################
Import pandas as pd
# Create empty DataFrame#
emt_df = pd.DataFrame()
print(emt_df)
#  Creating Pandas DataFrame from List#
df = pd.DataFrame(['a','b','f','t']) # create dataframe from list#
print(df)
#Creating Pandas DataFrame from List of List/ ndaray
ls_of_ls = [[1,2,3], [2,3,4], [4,5,6]]   # Creating list of list
print(ls_of_ls)
df2 = pd.DataFrame(ls_of_ls)   # Creating dataframe form above list of list
df2

#Creating Pandas DataFrame from Dict#
dict1 = {'ID': [11,22,33,44]}   # Creating dict 
df3 = pd.DataFrame(dict1)    # Creating dataframe from above dict
dict2 = {'ID': [11,22,33,44], 'SN': [1,2,3,4]} # for more data value#
df4 = pd.DataFrame(dict1)


#Creating Pandas DataFrame from List of Dicts
ls_dict = [{'a':1, 'b':2}, {'a':3, 'b':4}]   # Creating list of dict
df5 = pd.DataFrame(ls_dict)   # Creating dataframe from list of dict

# Creating dataframe from list of dict with different way - unequal#
ls_dict = [{'a':1, 'b':2}, {'a':3, 'b':4, 'c':5}]   
df6 = pd.DataFrame(ls_dict)
#Here in first dictionary ‘c’ is not defined but that command not gives error because pandas has function to handle missing values (which is shown by NaN)
#NaN means not a number

#Creating Pandas DataFrame from Dict of Series#
dict_sr = {'ID': pd.Series([1,2,3]), 'SN': pd.Series([111,222,333])}
df7 = pd.DataFrame(dict_sr)
