# 代码 4-30
import pandas as pd
dit = {'col1': [0, 1, 2, None, 4], 'col2': [5, None, 6, 7, None]}
df = pd.DataFrame(dit)
print('缺失值数量为：\n', df.isnull().sum())

print('缺失值占比为：\n', df.isnull().sum() / len(df))



# 代码 4-31
print('删除空值后的DataFrame为：\n', df.dropna())



# 代码 4-32
print('删除col1列空值后的DataFrame为：\n', df.dropna(subset=['col1']))



# 代码 4-33
print('将空值替换为0后的DataFrame为：\n', df.fillna(0))



# 代码 4-34
print('替换缺失值后的DataFrame为：\n', df.fillna(method='ffill'))



# 代码 4-35
# linear方法插值
print('linear方法插值后的DataFrame为：\n', df.interpolate())

# values方法插值
df1 = df.set_index(pd.Index([0, 1, 2, 8, 9]))
print('values方法插值后的DataFrame为：\n', df1.interpolate(method='values'))

# time方法插值
index = pd.to_datetime(['2018-01-01', '2018-01-02',
                        '2018-01-03', '2018-01-08', '2018-01-10'])
df2 = df.set_index(index)
print('time方法插值后的DataFrame为：\n', df2.interpolate(method='time'))



# 代码 4-36
df = pd.read_csv('../data/Station.csv', encoding='gbk')
df1 = df.drop_duplicates()
print('去重前数据框的长度为：', len(df), '\n', '去重后数据框的长度为：', len(df1))



# 代码 4-37
df2 = df.drop_duplicates(subset=['train'])
print('去重前数据框长度为：', len(df), '\n', '指定特征col1去重后数据框长度为：', len(df2))



# 代码 4-38
series = pd.Series([1, 6, 7, 8, 9, 15])
series1 = pd.cut(series, bins=3)
print('离散化前的数据为：\n', series, '\n', '等宽离散化后的数据为：\n', series1)

print('离散化后各区间数据数目为：\n', series1.value_counts())



# 代码 4-39
import numpy as np


def SameRateCut(data, k):
    w = data.quantile(np.arange(
            0, 1 + 1.0 / k, 1.0 / k))
    data = pd.cut(data, w)
    return data


series1 = SameRateCut(series, 3)
print('等频离散化后数据为：\n', series1, '\n',
      '离散化后数据各区间数目为：\n', series1.value_counts())



# 代码 4-40
dit = {'one': ['高', '低', '低', '高', '中'],
       'two': [1, 4, 6, 7, 8]}
df = pd.DataFrame(dit)
print('创建的DataFrame为：\n', df)
print('哑变量处理后的DataFrame为：\n', pd.get_dummies(df))
