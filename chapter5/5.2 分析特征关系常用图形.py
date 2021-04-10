# 代码 5-7
import matplotlib.pyplot as plt
import numpy as np
data = np.load('../data/国民经济核算季度数据.npz', allow_pickle=True)
name = data['columns']  # 提取columns数组，视为数据的标签
values = data['values']  # 提取values数组，数据的存在位置
plt.rcParams['font.sans-serif'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False
plt.figure(figsize=(8, 7))
plt.scatter(values[:, 0], values[:, 2], marker='o')
plt.xlabel('年份')
plt.ylabel('生产总值（亿元）')
plt.xticks(range(0, 70, 4), values[range(0, 70, 4), 1], rotation=45)
plt.title('2000~2017年季度生产总值散点图')
plt.savefig('../tmp/2000~2017年季度生产总值散点图.png')
plt.show()



# 代码 5-8
plt.Figure(dpi=80, figsize=(8, 7))
plt.rcParams['font.sans-serif'] = 'SimHei'
y1 = values[:, 3]
plt.scatter(range(len(y1)), y1)
# plt.xticks(range(len(y1)), values[:: 4, 1], rotation=45)
y2 = values[:, 4]
plt.scatter(range(len(y2)), y2)
# plt.xticks(range(len(y2)), values[:: 4, 1], rotation=45)
y3 = values[:, 5]
plt.scatter(range(len(y3)), y3)
plt.xticks(range(0, 70, 4), values[range(0, 70, 4), 1], rotation=45)
plt.title('2010~2017年各产业季度生产总值')
plt.legend(['第一产业', '第二产业', '第三产业'])
plt.savefig('../tmp/三种产业散点图.png')
plt.show()



# 代码 5-9
plt.rcParams['font.sans-serif'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False
plt.figure(dpi=80, figsize=(8, 8))
y1 = values[:: 4, 3]
y2 = values[:: 4, 4]
y3 = values[:: 4, 5]
plt.plot(range(len(y1)), y1, linestyle='-.')
plt.plot(range(len(y2)), y2, linestyle='--')
plt.plot(range(len(y3)), y3)
plt.xticks(range(len(y3)), values[:: 4, 1], rotation=45)
plt.title('2000~2017年各产业第一季度折线图')
plt.legend(['第一产业', '第二产业', '第三产业'])
plt.savefig('../tmp/各产业第一季度折线图.png')
plt.show()



# 代码 5-10
plt.figure(figsize=(8, 7))
plt.plot(values[:, 0], values[:, 3], 'b-',
         values[:, 0], values[:, 4], 'y-.',
         values[:, 0], values[:, 5], 'g--')
plt.xlabel('年份')
plt.ylabel('生产总值（亿元）')
plt.xticks(range(0, 70, 4), values[range(0, 70, 4), 1], rotation=45)
plt.title('2000~2017年各产业季度生产总值折线图')
plt.legend(['第一产业', '第二产业', '第三产业'])
plt.savefig('../tmp/2000~2017年季度各产业生产总值折线图.png')
plt.show()
