# -*- coding: utf-8 -*-
"""
Created on Tue May 25 15:52:29 2021

@author: dms10
"""

import pandas as pd

dict_data = {'A':[1,2,3], 'B':[4,5,6], 'c':[7,8,9], 'd':[10,11,12], 'e':[13,14,15]}

df = pd.DataFrame(dict_data)
print(type(df))
print('\n')
print(df)

#인덱스는 자동으로 매겨진다
