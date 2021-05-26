# -*- coding: utf-8 -*-
"""
Created on Tue May 25 15:58:29 2021

@author: dms10
"""

import pandas as pd

df = pd.DataFrame([[15, '남', '덕영중'], [17, '여', '수리중']],
                   index=['준서', '예은'],
                   columns=['나이', '성별', '학교'])
                    
print(df)
print('\n')
print(df.index)
print('\n')
print(df.columns)
print('\n')

'''
df.index=['학생1', '학생2']
df.columns=['연령', '남녀', '소속']

print(df)
print('\n')
print(df.index)
print('\n')
print(df.columns)
'''

df.rename(columns={'나이':'연령', '성별':'남녀', '학교':'소속'}, inplace=True)
df.rename(index={'준서':'학생1', '예은':'학생2'}, inplace=True)

print(df)