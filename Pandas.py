import numpy as np
import pandas as pd

# labels = ['a', 'b', 'c']
# my_data = [10, 20, 30]
# arr = np.array(my_data)
# d = {'a': 10, 'b': 20, 'c': 30}

# pd.Series(data=my_data, index=labels)
# pd.Series(arr, labels)
# pd.Series(d)

# ser1 = pd.Series([1, 2, 3, 4], ['USA', 'Germany', 'USSR', 'Japan'])
# ser2 = pd.Series([1, 2, 5, 4], ['USA', 'Germany', 'Italy', 'Japan'])

# print(ser1 + ser2)

# np.random.seed(101)
#
# df = pd.DataFrame(randn(5, 4), ['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])
# WColumn = df['W']
#
# BRow = df.loc['B']
# Brow = df.iloc[1]

# print(BRow)

# booldf = df > 0
# dfgrzero = df[df>0]
#
# resultdf = df[df['W'] > 0]
# print(resultdf)
# print(resultdf['X'])

# print(df[(df['W'] > 0) & (df['Y'] > 1)])

# newind = 'CA NY WY OR CO'.split()
# df['States'] = newind
#
# print(df)

# Index Levels
# outside = ['G1', 'G1', 'G1', 'G2', 'G2', 'G2']
# inside = [1, 2, 3, 1, 2, 3]
# hier_index = list(zip(outside, inside))
#
# df = pd.DataFrame(randn(6, 2), hier_index, ['A', 'B'])
# df.index.names = ['Groups']
# print(df)

# d = {'A': [1, 2, numpy.nan], 'B': [5, numpy.nan, numpy.nan], 'C': [1, 2, 3]}
# df = pd.DataFrame(d)
# print(df)

# data = {'Company': ['GOOG', 'GOOG', 'MSFT', 'MSFT', 'FB', 'FB'],
#         'Person': ['Sam', 'Charlie', 'Amy', 'Vanessa', 'Carl', 'Sarah'],
#         'Sales': [200, 120, 340, 124, 243, 350]}
#
# df = pd.DataFrame(data)
#
# byComp = df.groupby('Company')
# print(byComp.mean().loc['FB'])
# print(byComp.sum())
# print(byComp.std())

