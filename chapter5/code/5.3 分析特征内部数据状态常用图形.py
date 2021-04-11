# 代码 5-11
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False
plt.figure(figsize=(8, 6), dpi=100)
mu = 0
sigma = 1
x = np.random.normal(mu, sigma, 10000)  # 生成10000个服从标准正态分布数据
plt.hist(x, bins=20, density=True, rwidth=0.96)  # 绘制直方图
plt.title('标准正态分布数据直方图')
plt.savefig('../tmp/标准正态分布数据直方图.png')
# plt.show()



# 代码 5-12
data = np.load('../data/国民经济核算季度数据.npz', allow_pickle=True)
values = data['values']
plt.rcParams['font.sans-serif'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False
x = range(3)
my_height = np.sum(values[-2: -6: -1, 3: 6], axis=0)
plt.figure(figsize=(8, 8), dpi=100)
plt.bar(x, my_height, width=0.8)
for i in range(len(my_height)):
    plt.text(i, my_height[i], '{}亿元'.format(my_height[i]), va='bottom', ha='center')
plt.xticks(x, ['第一产业', '第二产业', '第三产业'])
plt.ylim([0, 500000])
plt.title('2016年各产业国民生产总值条形图')
plt.savefig('../tmp/2016年各产业国民生产总值条形图.png')
# plt.show()



# 代码 5-13
name = data['columns']
plt.rcParams['font.sans-serif'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False
pic = plt.figure(dpi=100, figsize=(8, 4))
plt.rcParams['font.sans-serif'] = 'SimHei'
a_labs = [i[: 4] for i in name[3: 6]]  # 定义标签
b_labs = [i[: 2] for i in name[6:]]
explode = [0.01, 0.01, 0.01]  # 设定各项离心0.01个半径
# 绘制2000年产业结构饼图
pic.add_subplot(1, 2, 1)
plt.pie(np.sum(values[: 4, 3: 6], axis=0), autopct='%1.1f%%',
        labels=a_labs, explode=explode)  # 绘制饼图
plt.title('2000年产业结构')
# 绘制2016年产业结构饼图
pic.add_subplot(1, 2, 2)
plt.pie(np.sum(values[-2: -6: -1, 3: 6], axis=0), autopct='%1.1f%%',
        labels=a_labs, explode=explode)
plt.title('2016年产业结构')
plt.savefig('../tmp/2000到2016产业结构变化饼图.png')
# plt.show()



# 代码 5-14
plt.rcParams['font.sans-serif'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False
pic = plt.figure(dpi=200, figsize=(8, 8))
plt.rcParams['font.sans-serif'] = 'SimHei'
a_labs = [i[: 4] for i in name[3: 6]]
b_labs = [i[: 2] for i in name[6:]]
pic.add_subplot(2, 1, 1)
plt.boxplot([list(values[:, 3]), list(values[:, 4]),
             list(values[:, 5])], notch=True, meanline=True)
plt.xticks(range(1, 4), a_labs)
plt.title('2000~2017年各产业国民生产总值箱线图')
pic.add_subplot(2, 1, 2)
tem = []
for i in range(6, len(values[0])):
    tem.append(list(values[:, i]))
plt.boxplot(tem, notch=True, meanline=True)
plt.xticks(range(1, len(b_labs) + 1), b_labs)
plt.title('2000~2017年各行业国民生产总值箱线图')
plt.savefig('../tmp/生产总值箱线图.png')
plt.show()
