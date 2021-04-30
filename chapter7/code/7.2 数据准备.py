# 代码 7-1
import pandas as pd
import matplotlib.pyplot as plt

# 导入数据
info = pd.read_csv('../data/meal_order_info.csv', encoding='utf-8')
info_before = pd.read_csv('../data/info_new.csv', encoding='utf-8')
# 合并数据
info_all = pd.concat([info_before, info])
print('查看各表的维数：\n', info.shape, info_before.shape, info_all.shape)

# 提取订单状态为1的数据
info = info_all[info_all['order_status'].isin(['1'])]
info = info.reset_index(drop=True)
# 统计每日用餐人数与营业额
for i, k in enumerate(info['use_start_time']):
    y = k.split()
    y = pd.to_datetime(y[0])
    info.loc[i, 'use_start_time'] = y

groupbyday = info[['use_start_time', 'number_consumers',
                   'accounts_payable']].groupby(by='use_start_time')
sale_day = groupbyday.sum()
sale_day.columns = ['人数', '销量']

# 每日用餐人数折线图
# 解决中文显示问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.figure(figsize=(12, 6))
plt.title('每日用餐人数折线图')
plt.xlabel('日期')
plt.ylabel('用餐人数')
plt.plot(sale_day['人数'])
plt.show()

# 画出每日销售额的折线图
# 新建画板
plt.figure(figsize=(12, 6))
plt.title('每日销售额的折线图')
plt.xlabel('日期')
plt.ylabel('销售额')
plt.plot(sale_day['销量'])
plt.show()



# 代码 7-2
info_august = pd.read_csv('../data/meal_order_info.csv', encoding='utf-8')
users_august = pd.read_csv('../data/users.csv', encoding='gbk')
# 提取订单状态为1的数据
info_august_new = info_august[info_august['order_status'].isin(['1'])]
info_august_new = info_august_new.reset_index(drop=True)
print('提取的订单数据维数：', info_august_new.shape)
info_august_new.to_csv('../tmp/info_august_new.csv', index=False, encoding='utf-8')

# 匹配用户的最后一次用餐时间
for i in range(1, len(info_august_new)):
    num = users_august[users_august['USER_ID'] ==
                       info_august_new.iloc[i-1, 1]].index.tolist()
    users_august.iloc[num[0], 14] = info_august_new.iloc[i-1, 9]
    users_august.iloc[num[0], 14] = info_august_new.iloc[i-1, 9]

user = users_august
user['LAST_VISITS'] = user['LAST_VISITS'].fillna(999)
user = user.drop(user[user['LAST_VISITS'] == 999].index.tolist())
user = user.iloc[:, [0, 2, 12, 14]]
print(user.head())
user.to_csv('../tmp/users_august.csv', index=False, encoding='utf-8')



# 代码 7-3
# 读取数据
users = pd.read_csv('../data/user_loss.csv', encoding='gbk')
info = pd.read_csv('../data/info_new.csv', encoding='utf-8')
print('历史客户信息表的维数：', users.shape)
print('历史订单表的维数：', info.shape)


# 将时间转为时间格式
users['CREATED'] = pd.to_datetime(users['CREATED'])
info['use_start_time'] = pd.to_datetime(info['use_start_time'])
info['lock_time'] = pd.to_datetime(info['lock_time'])

# 匹配用户的最后一次用餐时间
for i in range(len(users)):
    info1 = info.iloc[info[info['name'] == users.iloc[i, 2]].index.tolist(), :]
    if sum(info['name']==users.iloc[i, 2]) != 0:
        users.iloc[i, 14] = max(info1['use_start_time'])

# 特征选取
# 提取有效订单
info = info.loc[info['order_status'] == 1, ['emp_id', 'number_consumers', 'expenditure']]
info = info.rename(columns={'emp_id': 'USER_ID'})  # 修改列名
print(info.head())


user = users.iloc[:, [0, 2, 14, 37]]
print(user.head())

# 合并两个表
info_user = pd.merge(user, info, left_on='USER_ID', right_on='USER_ID', how='left')
info_user.to_csv('../tmp/info_user.csv', index=False, encoding='utf-8')
print(info_user.head())
