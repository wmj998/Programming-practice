# 代码 3-40
import pandas as pd
print('创建的Timestamp为：Timestamp({0})'.format(pd.Timestamp(2018, 8, 15, 12)))



# 代码 3-41
print('最小时间为：', pd.Timestamp.min)

print('最大时间为：', pd.Timestamp.max)



# 代码 3-42
import numpy as np
date = ['2016/8/1 11:11:46', '2017/9/2 12:13:48', '2015/7/3 09:08:40',
        np.nan, '2016/8/1 11:11:46']
series = pd.Series(date)
print('创建的Series为：\n', series)

series1 = pd.to_datetime(series)
print('转换为时间类型的Series为：\n', series1)



# 代码 3-43
date1 = pd.Timestamp(2018, 8, 15, 12, 21, 59)
print('从Timestamp提取的年为：', date1.year)

print('从Timestamp提取的月为：', date1.month)

print('从Timestamp提取的日为：', date1.day)

print('从Timestamp提取的小时为：', date1.hour)

print('从Timestamp提取的分钟为：', date1.minute)

print('从Timestamp提取的秒为：', date1.second)



# 代码 3-44
print('从Series提取的年为：\n', series1.dt.year)

print('从Series提取的月为：\n', series1.dt.month)

print('从Series提取的日为：\n', series1.dt.day)



# 代码 3-45
print('创建的Timedelta为：Timedelta({0})'.format(pd.Timedelta('1days 1minute')))



# 代码 3-46
print('创建的Timedelta为：Timedelta({0})'. format(pd.Timedelta(days=1, minutes=1)))



# 代码 3-47
series2 = pd.Series(['1days 1minute', '2days 3minute'])
# 转换成Timedelta
timedelta = pd.to_timedelta(series2)
print('转换后的Series为：\n', timedelta)



# 代码 3-48
time_delta = pd.Timestamp(2018, 8, 15, 12) - pd.Timestamp(2018, 8, 14, 12)
print('Timestamp相减后结果为：TimeDelta({0})'.format(time_delta))



# 代码 3-49
print('Timedelta相减后为：TimeDelta({0})'. format(timedelta[1] - timedelta[0]))



# 代码 3-50
print('Timestamp与Timedelta相减后为：',
      'Timestamp({0})'.format(pd.Timestamp(2018, 8, 15, 12) + timedelta[0]))



# 代码 3-51
# 转换为小时
print('Timedelta频率转换为小时后的数值为：\n', timedelta / pd.Timedelta('1 hour'))

# 转换为分钟
print('Timedelta频率转换为分钟后的数值为：\n', timedelta / pd.Timedelta('1 minute'))



# 代码 3-52
# 转换为小时
print('Timedelta频率转换为小时后的数值为：\n', timedelta.astype(('timedelta64[h]')))

# 转换为分钟
print('Timedelta频率转换为分钟后的数值为：\n', timedelta.astype(('timedelta64[m]')))



# 代码 3-53
print('从Timedelta提取的天数为：', timedelta[0].days)

print('从Timedelta提取的秒数为：', timedelta[0].seconds)

print('从Timedelta提取的微秒数为：', timedelta[0].microseconds)

print('从Timedelta提取的纳秒数为：', timedelta[0].nanoseconds)



# 代码 3-54
print('从Series提取的天为：\n', timedelta.dt.days)

print('从Series提取的秒为：\n', timedelta.dt.seconds)



# 代码 3-55
timeindex = pd.DatetimeIndex(['2018-01-01', '2018-01-02', '2018-01-03', '2018-01-04'])
print('创建的DatetimeIndex为：\n', timeindex)



# 代码 3-56
print('创建的DatetimeIndex为：\n', pd.date_range(start='2018-01-01', end='2018-01-08'))



# 代码 3-57
print('创建的DatetimeIndex为：\n', pd.date_range(start='2018-01-01', periods=8))



# 代码 3-58
print('创建的DatetimeIndex为：\n',
      pd.date_range(start='2018-01-01', periods=8, freq='M'))



# 代码 3-59
date = pd.date_range(start='2018-01-10 01:02:03', periods=5, freq='W')
list1 = [1, 2, 3, 4, 5]
arr = pd.Series(list1, index=date)
print('创建的时间序列为：\n', arr)



# 代码 3-60
print('访问2018-01-14 01:02:03的数据为：', arr['2018-01-21 01:02:03'])



# 代码 3-61
print('访问2018年1月份数据为：\n', arr['2018-1'])



# 代码 3-62
print('访问2017年12月到2018年2月3号的数据为：\n', arr['2017-12': '2018-02-03'])



# 代码 3-63
series3 = pd.Series(['a', 'abb', 'Ab12'])
print('大写后的Series为：\n', series3.str.upper())



# 代码 3-64
# 匹配以小写a开头的元素，将ab替换为F，作用于Series
print('替换后的Series为：\n', series3.str.replace(r'^ab', 'F'))

print('替换后的元素为：\n', series3.str.replace(r'^ab', 'F')[1])

# 匹配以小写a开头的元素，将ab替换为F，作用于str
print('替换后的str为：', series3[1].replace(r'^ab', 'F'))



# 代码 3-65
print('cat方法作用后的结果为：', series3.str.cat(sep='-'))

print('get方法作用后的结果为：\n', series3.str.get(1))

print('get_dummies方法作用后的结果为：\n', series3.str.get_dummies())

print('contains方法作用后的结果为：\n', series3.str.contains('ab', regex=False))

print('repeat方法作用后的结果为：\n', series3.str.repeat(2))

print('pad方法作用后的结果为：\n', series3.str.pad(width=2, side='left', fillchar='f'))



# 代码 3-66
# 位置索引
print('第一个字符为：\n', series.str[0])

# 切片索引
print('前两个字符为：\n', series3.str[0: 2])



# 代码 3-67
series4 = pd.Series(['a', 'b', 'b', 'c'], dtype='category')
print('指定Series数据类型创建的category为：\n', series4)



# 代码 3-68
series = pd.Series(['a', 'b', 'b', 'c'])
series1 = series.astype('category')
print('转换Series数据类型创建的category为：\n', series1)

from pandas.api.types import CategoricalDtype
cat_type = CategoricalDtype(categories=['b', 'c', 'd'], ordered=True)
series1 = series.astype(cat_type)
print('转换Series数据类型为CategoricalDtype创建的category结果为：\n', series1)


# 代码 3-69
raw_cat = pd.Categorical(['a', 'b', 'b', 'c'],
                         categories=['a', 'b', 'c'], ordered=False)
series = pd.Series(raw_cat)
print('接收Categorical对象创建category为：\n', series)



# 代码 3-70
series = pd.Series(range(9))
series1 = pd.cut(series, [0, 3, 6, 9, 12], right=False)
print('cut函数作用Series创建category结果为：\n', series1)



# 代码 3-71
series = pd.Series(['a', 'b', 'b', 'c'], dtype='category')
print('category的类别为：\n', series.cat.categories)

print('category的类别是否指定：', series.cat.ordered)



# 代码 3-72
series1 = series.cat.rename_categories([1, 2, 3])
print('重命名category的类别为：', series1.cat.categories)



# 代码 3-73
series1 = series.cat.add_categories(['e'])
print('新增后的category的类别为：\n', series1.cat.categories)



# 代码 3-74
series1 = series.cat.remove_categories(['c'])
print('删除后的category的类别为：\n', series1.cat.categories)



# 代码 3-75
series1 = series.cat.set_categories(['c', 'd'], ordered=True)
print('设置后的category的类别为：\n', series1.cat.categories)



# 代码 3-76
series1 = series.cat.set_categories(['c', 'e', 'a', 'b'], ordered=True)
print('指定顺序后的category为：\n', series1.sort_values())
