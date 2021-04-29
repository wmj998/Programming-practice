import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False

Meals_income = pd.read_csv('../data/Meals_income.csv')

fig = plt.figure()

# 画柱形图
ax1 = fig.add_subplot(111)
ax1.set_ylim([0, 4500])
ax1.bar(Meals_income['year'], Meals_income['income'], label='收入（亿元）') # 增加label参数，方便增加图例
ax1.set_ylabel('收入（亿元）')
ax1.legend(bbox_to_anchor=(0.5, 1)) # 添加第一个图例，并设定其位置

# 画折线图
ax2 = ax1.twinx()  # 组合图必须加这个
ax2.set_ylim([0, 1.1])
ax2.plot(Meals_income['year'], Meals_income['growth'], 'r', ms=10, lw=3, label='同比增长率') # 增加label参数，方便增加图例
ax2.set_ylabel('同比增长率')
ax2.legend(bbox_to_anchor=(0.8, 1)) # 添加第二个图例，并设定其位置

plt.savefig('../tmp/Meals_income.png', dpi=1000, bbox_inches='tight')
plt.show()
