# 代码 4-8
import pandas as pd
import numpy as np
df = pd.read_csv('D:/文件丶/课件/《Python机器学习编程与实战》源数据和代码/第4章/示例程序/data/Concrete.csv', encoding='gbk')
print('数据框df每列对应的最大值为：\n', np.max(df))
print('数据框df每列对应的最小值为：\n', np.min(df))

print('数据框df每列对应的均值为：\n', np.mean(df))

print('数据框df对应的中位数为：', np.median(df))

print('数据框df每列对应的标准差为：\n', np.std(df))

print('数据框df每列对应的方差为：\n', np.var(df))



# 代码 4-9
print('数据框df每列对应的最大值为：\n', df.max())
print('数据框df每列对应的最小值为：\n', df.min())

print('数据框df每列对应的均值为：\n', df.mean())

print('数据框df每列对应的中位数为：\n', df.median())

print('数据框df每列对应的标准差为：\n', df.std())

print('数据框df每列对应的方差为：\n', df.var())



# 代码 4-10
print('使用describe方法的描述性统计结果为：\n', df.describe())



# 代码 4-11
df1 = pd.DataFrame({'col1': list('abca'), 'col2': list('bccd')}, dtype='category')
print('使用describe方法的描述性统计结果为：\n', df1.describe())



# 代码 4-12
print('DataFrame的info信息为：\n')
df.info()



# 代码 4-13
arr = np.array([[2, 2, 2], [4, 4, 4], [6, 6, 6], [8, 8, 8], [10, 10, 10]])
df2 = pd.DataFrame(arr, columns=['one', 'two', 'three'],
                   index=pd.date_range('1/1/2018', periods=5))
print('创建的移动窗口对象为：', df2.rolling(2))



# 代码 4-14
print('移动窗口为2，使用mean方法计算后结果为：\n', df2.rolling(2).mean())

print('移动窗口为2，使用sum方法计算后结果为：\n', df2.rolling(2).sum())



# 代码 4-15
print('移动窗口为2天，使用mean方法计算后结果为：\n', df2.rolling('2D').mean())

print('移动窗口为2天，使用sum方法计算后结果为：\n', df2.rolling('2D').sum())



# 代码 4-16
station = pd.read_csv('D:/文件丶/课件/《Python机器学习编程与实战》源数据和代码/第4章/示例程序/data/Station.csv', encoding='gbk')
group = station.groupby('station')
print('以station为分组键，创建的GroupBy对象为：\n', group)



# 代码 4-17
print('分组数据的均值前5行结果为：\n', group.mean().head())

print('分组数据的和前5行结果为：\n', group.sum().head())

print('分组数据的最大值前5行结果为：\n', group.max().head())



# 代码 4-18
print('分组的均值前5行结果为：\n', group.agg(np.mean).head())



# 代码 4-19
def f(x):
    return x.max() - x.min()


group1 = group.agg(f)
print('分组的极差前5行结果为：\n', group1.head())



# 代码 4-20
group2 = group.agg([np.mean, np.sum])
print('分组的均值和总和前5行结果为：\n', group2.head())



# 代码 4-21
group3 = group.agg({'on_man': np.mean, 'off_man': np.sum})
print('列on_man应用均值函数，列off_man应用汇总函数前5行结果为：\n', group3.head())



# 代码 4-22
print('分组的均值前5行结果为：\n', group.apply(np.mean).head())



# 代码 4-23
def f(x):
    result = x[0: 2]
    return result


print('分组的前两个数据前5行结果为：\n', group.apply(f).head())



# 代码 4-24
print('对分组应用均值函数，返回的DataFrame前5行数据为：\n',
      group.transform(np.mean).head())



# 代码 4-25
def f(x):
    result = x*2
    return result


print('对分组的每个元组乘以2，返回的DataFrame前5行数据为：\n',
      group.transform(f).head())



# 代码 4-26
dit = {'one': ['a', 'b', 'b', 'b', 'a'], 'two': [0, 1, 2, 3, 4],
     'three': [5, 6, 7, 8, 9], 'four': ['x', 'x', 'y', 'y', 'y']}
df = pd.DataFrame(dit)
tdf = pd.pivot_table(df, index=['four'], columns=['one'])
print('创建的透视表为：\n', tdf)



# 代码 4-27
tdf = pd.pivot_table(df, index=['four'], columns=['one'], aggfunc=np.sum)
print('分组和的透视表为：\n', tdf)



# 代码 4-28
cdf = pd.crosstab(index=df['four'], columns=df['one'])
print('创建的交叉表为：\n', cdf)



# 代码 4-29
cdf = pd.pivot_table(df, values='two', index=['four'], columns=['one'],
                     aggfunc=(lambda x: len(x)))
print('使用pivot_table函数创建的交叉表为：\n', cdf)
