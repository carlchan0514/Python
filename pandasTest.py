# Series of Pandas
import pandas as pd
import numpy as np
s1 = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
print(s1)

s2 = pd.Series({'a':3,'b':4,'c':5,'f':6,'e':8})
print(s2)

print(s1['a'])
print(s1[['a', 'b']])

print(s1.head(2))
print(s2.tail())

print(s2.index)
print(s2.values)

print("len():",len(s1))# Series长度,包括NaN
print("shape():",np.shape(s1))# 矩阵形状，（，）
print("count():",s1.count())# Series长度，不包括NaN
print("unique():",s1.unique())# 出现不重复values值
print("value_counts():\n",s1.value_counts())# 统计value值出现次


s1 = pd.Series([1, 2, 3, 4], index=[1, 2, 3, 4])
s2 = pd.Series([1, 1, 1, 1])
s3 = s1+s2
print(s3)

# DataFrame of Pandas
s1 = np.array([1, 2, 3, 4])
s2 = np.array([5, 6, 7, 8])
df = pd.DataFrame([s1, s2])
print(df)
print([s1, s2])

s1 = pd.Series(np.array([1, 2, 3, 4]))
s2 = pd.Series(np.array([5, 6, 7, 8]))
df = pd.DataFrame([s1, s2])
print(df)

s1 = pd.Series(np.array([1, 2, 3, 4]))
s2 = pd.Series(np.array([5, 6, 7, 8]))
df = pd.DataFrame({"a": s1, "b": s2})
print(df)

df = pd.DataFrame({"A": [1, 2, 3, 4], "B": [5, 6, 7, 8], "C": [1, 1, 1, 1]})
df.ix[df.A > 1, 'B'] = -1
print(df)

df = pd.DataFrame({"A": [1, 2, 3, 4], "B": [5, 6, 7, 8], "C": [1, 1, 1, 1]})
df["then"] = np.where(df.A < 3, 1, 0)
print(df)

df = pd.DataFrame({"A": [1, 2, 3, 4], "B": [5, 6, 7, 8], "C": [1, 1, 1, 1]})
df = df[df.A >= 2]
print(df)

df = pd.DataFrame({"A": [1, 2, 3, 4], "B": [5, 6, 7, 8], "C": [1, 1, 1, 1]})
df = df.loc[df.A > 2]
print(df)