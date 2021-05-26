# -*- coding: utf-8 -*-
"""
Created on Tue May 25 17:08:43 2021

@author: dms10
"""

exam_data = {'이름' : ['서준', '우현', '인아'],
             '수학' : [ 90, 80, 70],
             '영어' : [ 98, 89, 95],
             '음악' : [ 85, 95, 100],
             '체육' : [ 100, 90, 90]}

df = pd.DataFrame(exam_data)
print(df)
print(type(df))
print('\n')

math1 = df['수학']
print(math1)
print(type(math1))
print('\n')

english = df.영어
print(type(english))
print('\n')

music_gym = df[['음악', '체육']]
print(music_gym)
print(type(music_gym))
print('\n')

math2 = df[['수학']]
print(math2)
print(type(math2))

df.set_index('이름', inplace = True)
print(df)

a = df.loc['서준', '음악']
print(a)
b = df.iloc[0, 2]
print(b)

c = df.loc['서준', ['음악', '체육']]
print(c)

d = df.iloc[0, [2,3]]
print(d)

e = df.loc['서준', '음악':'체육']
print(e)

f = df.iloc[0, 2:]
print(f)

g = df.loc[['서준', '우현'], ['음악', '체육']]
print(g)

h = df.iloc[[0, 1], [2, 3]]
print(h)

i = df.loc['서준':'우현', '음악':'체육']
print(i)

j = df.iloc[0:2, 2:]
print(j)

df['국어'] = 80
print(df)

df.loc[3] = 0
print(df)
print('\n')

df.loc[4] = ['동규', 90, 80, 70, 60]
print(df)
print('\n')

df.loc['행5'] = df.loc[3]
print(df)

df.set_index('이름', inplace = True)
print(df)
print('\n')

df.iloc[0][3] = 80
print(df)
print('\n')

df.loc['서준']['체육'] = 90
print(df)
print('\n')

df.loc['서준', '체육'] = 100
print(df)