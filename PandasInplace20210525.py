# -*- coding: utf-8 -*-
"""
Created on Tue May 25 16:40:02 2021

@author: dms10
"""

import pandas as pd

exam_data = {'수학' : [ 90, 80, 70], '영어' : [ 98, 89, 95],
             '음악' : [ 85, 95, 100], '체육' : [ 100, 90, 90]}

df = pd.DataFrame(exam_data, index=['서준','우현','인아'])
print(df)
print('\n')

df2 = df.copy()
df2.drop('우현', axis = 0, inplace=True)
print(df2)
print('\n')

df3 = df.copy()
df3.drop(['우현', '인아'], axis = 0, inplace=True)
print(df3)
print('\n')

df4 = df.copy()
df4.drop('수학', axis = 1, inplace = True)
print(df4)
print('\n')

df5 = df.copy()
df5.drop(['영어','음악'], axis = 1 , inplace = True)
print(df5)
print('\n')

label1 = df.loc['서준']
position1 = df.iloc[0]
print(label1)
print('\n')
print(position1)

label2 = df.loc[['서준', '우현']]
position2 = df.iloc[[0,1]]
print(label2)
print('\n')
print(position2)

label3 = df.loc['서준':'우현']
position3 = df.iloc[0:1]
print(label3)
print('\n')
print(position3)