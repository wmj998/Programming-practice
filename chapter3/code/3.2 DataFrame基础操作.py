# 代码 3-21
import pandas as pd
df = pd.DataFrame({'col1': [0, 1, 2, 3, 4], 'col2': [5, 6, 7, 8, 9]},
                  index=['a', 'b', 'c', 'd', 'e'])
print('创建的DataFrame为：\n', df)

# 访问单列数据
print('DataFrame中col1列数据为：\n', df['col1'])



# 代码 3-22
# 以属性的方式访问单列数据
print('DataFrame中col1列数据为：\n', df.col1)



# 代码 3-23
# 访问单列多行数据
print('DataFrame中col1列前3行数据为：\n', df['col1'][0: 3])



# 代码 3-24
# 访问多列多行数据
print('DataFrame中col1列、col2列前3行数据为：\n', df[['col1', 'col2']][0: 3])



# 代码 3-25
# 访问多行数据
print('DataFrame的前3行为：\n', df[:][0: 3])



# 代码 3-26
# 访问单列数据
print('DataFrame中col1列数据为：\n', df.loc[:, 'col1'])

# 访问多列数据
print('DataFrame中col1列、col2数据为：\n', df.loc[:, ['col1', 'col2']])

# 访问单行数据
print('DataFrame中a行对应数据为：\n', df.loc['a', :])

# 访问多行数据
print('DataFrame中a行、b行对应数据为：\n', df.loc[['a', 'b'], :])

# 行列结合访问数据
print('DataFrame中a行、b行，col1列、col2列对应的数据为：\n',
      df.loc[['a', 'b'], ['col1', 'col2']])



# 代码 3-27
# 接收bool数据
print('DataFrame中col1列大于0的数据为：\n', df.loc[df['col1'] > 0, :])

# 接收函数
print('DataFrame中col1列大于0的数据为：\n', df.loc[lambda df: df['col1'] > 0, :])



# 代码 3-28
# 访问单列数据
print('DataFrame中col1列数据为：\n', df.iloc[:, 0])

# 访问多列数据
print('DataFrame中col1列、col2列数据为：\n', df.iloc[:, [0, 1]])

# 访问单行数据
print('DataFrame中a行数据为：\n', df.iloc[0, :])

# 访问多行数据
print('DataFrame中a行、b行数据为：\n', df.iloc[[0, 1], :])

# 行列结合访问数据
print('DataFrame中a行、b行，col1列、col2列数据为：\n', df.iloc[[0, 1], [0, 1]])



# 代码 3-29
# 接收bool数据
print('DataFrame中col1列大于0的数据为：\n', df.iloc[df['col1'].values > 0, :])

# 接收函数
print('DataFrame中col1列大于0的数据为：\n', df.iloc[lambda df: df['col1'].values > 0, :])



# 代码 3-30
# 按行索引排序
print('按行索引排序后的DataFrame为：\n', df.sort_index(axis=0))



# 代码 3-31
# 按列索引降序排列
print('按列索引降序排列后的DataFrame为：\n', df.sort_index(axis=1, ascending=False))



# 代码 3-32
# 按列排序
print('按col2列排序后的DataFrame为：\n', df.sort_values('col2'))



# 代码 3-33
# 按行降序排列
print('按列降序排列后的DataFrame为：\n', df.sort_values('a', axis=1, ascending=False))



# 代码 3-34
print('按col2列排序,返回前2个最小值：\n', df.nsmallest(2, 'col2'))

print('按col2列排序,返回前2个最大值：\n', df.nlargest(2, 'col2'))



# 代码 3-35
df2 = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3', 'K4', 'K5'],
                    'A': ['A0', 'A1', 'A2', 'A3', 'A4', 'A5']})
df3 = pd.DataFrame({'key': ['K0', 'K1', 'K2'], 'B': ['B0', 'B1', 'B2']})
# 横向堆叠df2、df3
print('横向堆叠df2、df3后的DataFrame为：\n', pd.concat([df2, df3], axis=1))

# 横向堆叠（内连）df2、df3
print('横向堆叠（内连）df2、df3后的DataFrame为：\n',
      pd.concat([df2, df3], axis=1, join='inner'))



# 代码 3-36
print('横向堆叠df2、df3后的DataFrame为：\n', df2.join(df3, rsuffix='_2'))



# 代码 3-37
# 纵向堆叠df2、df3
print('纵向堆叠df2、df3后的DataFrame为：\n', pd.concat([df2, df3], axis=0))

# 纵向堆叠（内连）df2、df3
print('纵向堆叠（内连）df2、df3后的DataFrame为：\n',
      pd.concat([df2, df3], axis=0, join='inner'))



# 代码 3-38
print('纵向堆叠df2、df3后的DataFrame为：\n', df2.append(df3))



# 代码 3-39
print('以列key为键，内连df2、df3后的DataFrame为：\n',
      pd.merge(df2, df3, on='key', how='inner'))
