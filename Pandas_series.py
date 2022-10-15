import pandas as pd
#To know the version of pandas#
pd.__version__

###############################################################################################################################
#Seris:  1-D homogenous data structure
###############################################################################################################################
#Pandas in Series data structure#

list_s = [1,2,-3,6.2,'data_value'] # create list#
print(list_s) 

#convert list to series#
s1 = pd.Series(list_s)
print(s1)

#convert list to sieres-2#
s2 = pd.Series([1,2,-3,4.5,'alisha'])
print(s2)

#creat empty series#
emp = pd.Series([])
print(emp)

#to change index#
s3 = pd.Series([1,2,-3,4.5,'alisha'], index = ['a','e','r','z','w'])
print(s3)

#to change into different datatype#
s4 = pd.Series([1,2,-3,4.5,7], index = ['a','e','r','z','w'], dtype= float)
print(s4)

#to give name to the series#
s5 = pd.Series([1,2,-3,4.5,7], index = ['a','e','r','z','w'], dtype= float, name = 'data values')
print(s5)

#Use scalar value to create series#
scalar_s= pd.Series(0.5)
print(scalar_s)

#Use scalar value in multiple series#
scalar_2 = pd.Series(0.5, index= [1,2,3,4])
print(scalar_2)

#use dict to create series#
dict_s = pd.Series({'a': 1, 'b': 2, 'c': 3})
print(dict_s)

####### Use operator to acess the keys###
s4[0]  # to access element in the series, [index value start: index value end-1]

max(s4) # use to access the maximum value in the series#
min(s4) # use to access the minimum value in the series#

#use conditional operator to generate element greater than 3#
s4[s4 > 3] # you can use mathematical operator also like addition, substraction, multiplication#
# It is good to have equal series and easy to use mathematical operators, otherwise it will generate nan value in unqual series#
