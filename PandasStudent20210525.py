# -*- coding: utf-8 -*-
"""
Created on Tue May 25 15:35:00 2021

@author: dms10
"""

import pandas as pd
tup_data = ('민수', '2017-04-08', '여', True)
sr = pd.Series(tup_data, index = ['이름', '생년월일', '성별', '학생여부'])
print(sr)

print(sr[0])
print(sr['이름'])

'''
print(sr[[1, 2]])
print('\n')
print(sr[['생년월일', '성별']])
'''

print(sr[1:])
print('\n')
print(sr['생년월일' : '학생여부'])