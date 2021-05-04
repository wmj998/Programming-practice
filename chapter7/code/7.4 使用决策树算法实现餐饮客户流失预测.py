# 代码 7-8
import pandas as pd

# 构建特征
info_user = pd.read_csv('../tmp/info_user.csv', encoding='utf-8')

# 提取info表的用户名和用餐时间，并按人名对用餐人数和金额进行分组求和
info_user1 = info_user['USER_ID'].value_counts()  # 统计每个人的用餐次数
info_user1 = info_user1.reset_index()
info_user1.columns = ['USER_ID', 'frequence']  # 修改列名

# 求出每个人的消费总金额
# 分组求和
info_user2 = info_user[['number_consumers',
                        "expenditure"]].groupby(info_user['USER_ID']).sum()
info_user2 = info_user2.reset_index()
info_user2.columns = ['USER_ID', 'numbers', 'amount']
# 合并两个表
info_user_new = pd.merge(info_user1, info_user2,
                         left_on='USER_ID', right_on='USER_ID', how='left')

# 对合并后的数据进行处理
info_user = info_user.iloc[:, :4]
info_user = info_user.groupby(['USER_ID']).last()
info_user = info_user.reset_index()
# 合并两个表
info_user_new = pd.merge(info_user_new, info_user,
                         left_on='USER_ID', right_on='USER_ID', how='left')
print(info_user_new.head())

# 去除空值
print('合并后表中的空值数目：', info_user_new.isnull().sum().sum())
info_user_new = info_user_new.dropna(axis=0)
# 删除numbers为0的客户
info_user_new = info_user_new[info_user_new['numbers'] != 0]

# 求平均消费金额，并保留2为小数
info_user_new['average'] = info_user_new['amount']/info_user_new['numbers']
info_user_new['average'] = info_user_new['average'].apply(
        lambda x: '%.2f' % x)

# 计算每个客户最近一次点餐的时间距离观测窗口结束的天数
# 修改时间列，改为日期
info_user_new['LAST_VISITS'] = pd.to_datetime(info_user_new['LAST_VISITS'])
datefinally = pd.to_datetime('2016-7-31')  # 观测窗口结束时间
time = datefinally - info_user_new['LAST_VISITS']
info_user_new['recently'] = time.apply(lambda x: x.days)   # 计算时间差
# 特征选取
info_user_new = info_user_new.loc[:, ['USER_ID', 'ACCOUNT', 'frequence',
                                      'amount', 'average', 'recently', 'type']]
info_user_new.to_csv('../tmp/info_user_clear.csv', index=False, encoding='gbk')
print(info_user_new.head())



# 代码 7-9
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier as DTC
from sklearn.metrics import confusion_matrix

# 划分测试集、训练集
info_user = pd.read_csv('../tmp/info_user_clear.csv', encoding='gbk')

# 删除流失用户
info_user = info_user[info_user['type'] != "已流失"]
model_data = info_user.iloc[:, [2, 3, 4, 5, 6]]
x_tr, x_te, y_tr, y_te = train_test_split(model_data.iloc[:, :-1],
                                          model_data['type'],
                                          test_size=0.2, random_state=12345)
# 初始化决策树对象，基于信息熵
dtc = DTC()
dtc.fit(x_tr, y_tr)  # 训练模型
pre = dtc.predict(x_te)
print('预测结果：\n', pre)



# 代码 7-10
# 混淆矩阵
hx = confusion_matrix(y_te, pre, labels=['非流失', '准流失'])
print('混淆矩阵：\n', hx)

# 精确率
P = hx[1, 1] / (hx[0, 1] + hx[1, 1])
print('精确率：', round(P, 3))
# 召回率
R = hx[1, 1] / (hx[1, 0] + hx[1, 1])
print('召回率：', round(R, 3))
# F1值
F1 = 2 * P * R / (P + R)
print('F1值：', round(F1, 3))