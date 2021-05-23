# 代码 3-1
import pandas as pd
import numpy as np

print('通过ndarray创建的Series为：\n',
      pd.Series(np.arange(5), index=['a', 'b', 'c', 'd', 'e'], name='ndarray'))

# 代码 3-2
dit = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4}
print('通过dict创建的Series为：\n', pd.Series(dit))

# 代码 3-3
list1 = [0, 1, 2, 3, 4]
print('通过list创建的Series为：\n', pd.Series(list1, index=['a', 'b', 'c', 'd', 'e'], name='list'))

# 代码 3-4
series = pd.Series(list1, index=['a', 'b', 'c', 'd', 'e'], name='list')
print('数组形式返回Series为：', series.values)

print('Series的Index为：', series.index)

print('Series的形状为：', series.shape)

print('Series的维度为：', series.ndim)

# 代码 3-5
print('Series位于第1位置的数据为：', series[0])

# 代码 3-6
print('Series中Index为a的数据为：', series['a'])

# 代码 3-7
bool = (series < 4)
print('bool类型的Series为：\n', bool)

print('通过bool访问Series结果为：\n', series[bool])

# 代码 3-8
# 更新元素
series['a'] = 3
print('更新后的Series为：\n', series)

# 代码 3-9
series1 = pd.Series([4, 5], index=['f', 'g'])
# 追加Series
print('在series插入series1后为：\n', series.append(series1))

# 新增单个数据
series1['h'] = 7
print('在series1插入单个数据后为：\n', series1)

# 代码 3-10
# 删除数据
series.drop('e', inplace=True)
print('删除索引e对应数据后的series为：\n', series)

# 代码 3-11
dict1 = {'col1': [0, 1, 2, 3, 4], 'col2': [5, 6, 7, 8, 9]}
print('通过dict创建的DataFrame为：\n', pd.DataFrame(dict1, index=['a', 'b', 'c', 'd', 'e']))

# 代码 3-12
list2 = [[0, 5], [1, 6], [2, 7], [3, 8], [4, 9]]
print('通过list创建的DataFrame为：\n',
      pd.DataFrame(list2, index=['a', 'b', 'c', 'd', 'e'], columns=['col1', 'col2']))

# 代码 3-13
df = pd.DataFrame({'col1': [0, 1, 2, 3, 4], 'col2': [5, 6, 7, 8, 9]},
                  index=['a', 'b', 'c', 'd', 'e'])
print('DataFrame的Index为：', df.index)

print('DataFrame的列标签为：', df.columns)

print('DataFrame的轴标签为：', df.axes)

print('DataFrame的维度为：', df.ndim)

print('DataFrame的形状为：', df.shape)

# 代码 3-14
print('默认返回前5行数据为：\n', df.head())

print('返回后3行数据为：\n', df.tail(3))

# 代码 3-15
# 更新列
df['col1'] = [10, 11, 12, 13, 14]
print('更新列后的DataFrame为：\n', df)

# 代码 3-16
# 插入列
df['col3'] = [15, 16, 17, 18, 19]
print('插入列后的DataFrame为：\n', df)

# 代码 3-17
# 删除列
df.drop(['col3'], axis=1, inplace=True)
print('删除col3列后的DataFrame为：\n', df)

# 删除行
df.drop('a', axis=0, inplace=True)
print('删除a行后的DataFrame为：\n', df)

# 代码 3-18
print('series的Index为 ：\n', series.index)

# 代码 3-19
print('series中Index各元素是否大于前一个：', series.index.is_monotonic)

print('series中Index各元素是否唯一：', series.index.is_unique)

# 代码 3-20
index1 = series.index
index2 = series1.index
print('index1连接index2后结果为：\n', index1.append(index2))

print('index1与index2的差集为：', index1.difference(index2))

print('index1与index2的交集为：', index1.intersection(index2))

print('index1与index2的并集为：\n', index1.union(index2))

print('index1中的元素是否在index2中：', index1.isin(index2))
