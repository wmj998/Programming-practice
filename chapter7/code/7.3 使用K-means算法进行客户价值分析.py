# 代码 7-4
import pandas as pd
from sklearn.preprocessing import StandardScaler
import numpy as np

info = pd.read_csv('../tmp/info_august_new.csv', encoding='utf-8')
user = pd.read_csv('../tmp/users_august.csv', encoding='utf-8')

# 构建RFM特征
# 构建F特征
# 统计每个人的用餐次数
user_value1 = pd.DataFrame(info['emp_id'].value_counts()).reset_index()
user_value1.columns = ['USER_ID', 'F']  # 修改列名
print('F特征的最大值：', max(user_value1['F']))
print('F特征的最小值：', min(user_value1['F']))

# 构建M特征
user_value2 = info[['emp_id', 'expenditure']].groupby(by='emp_id').sum()
user_value2 = pd.DataFrame(user_value2).reset_index()
user_value2.columns = ["USER_ID", "M"]
user_value = pd.merge(user_value1, user_value2, on='USER_ID')
print('M特征的最大值：', max(user_value['M']))
print('M特征的最小值：', min(user_value['M']))

# 构建R特征
user_value = pd.merge(user_value, user, on='USER_ID')  # 合并两个表
# 转换时间格式
for i, k in enumerate(user_value['LAST_VISITS']):
    y = k.split()
    y = pd.to_datetime(y[0])
    user_value.loc[i, 'LAST_VISITS'] = y
last_time = pd.to_datetime(user_value['LAST_VISITS'])
deadline = pd.to_datetime("2016-8-31")  # 观测窗口结束时间
user_value['R'] = deadline - last_time
print('R特征的最大值：', max(user_value['R']))
print('R特征的最小值：', min(user_value['R']))



# 代码 7-5
# 特征提取
user_value = user_value.iloc[:, [0, 3, 6, 1, 2]]
user_value.to_csv("../tmp/user_value.csv", encoding="utf-8_sig", index=False)

USER_ID = user_value['USER_ID']
ACCOUNT = user_value['ACCOUNT']
user_value = user_value.iloc[:, [2, 3, 4]]
user_value.iloc[:, 0] = [i.days for i in user_value.iloc[:, 0]]

# 标准差标准化
standard = StandardScaler().fit_transform(user_value)
np.savez('../tmp/standard.npz', standard)
print(standard)



# 代码 7-6
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans

standard = np.load('../tmp/standard.npz')['arr_0']
k = 3  # 聚类中心数

# 构建模型
kmeans_model = KMeans(n_clusters=k, n_jobs=3, random_state=123)
fit_kmeans = kmeans_model.fit(standard)  # 模型训练
print('聚类中心：\n', kmeans_model.cluster_centers_)

print('样本的类别标签：\n', kmeans_model.labels_)

# 统计不同类别样本的数目
r1 = pd.Series(kmeans_model.labels_).value_counts()
print('最终每个类别的数目为：\n', r1)



# 代码 7-7
%matplotlib inline
import matplotlib.pyplot as plt

# 中文和负号的正常显示
plt.rcParams['font.sans-serif'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False

# 绘制雷达图
N = len(kmeans_model.cluster_centers_[0])
# 设置雷达图的角度，用于平分切开一个圆面
angles = np.linspace(0, 2 * np.pi, N, endpoint=False)
# 为了使雷达图一圈封闭起来
angles = np.concatenate((angles, [angles[0]]))

# 绘图
fig = plt.figure(figsize=(7, 7))
ax = fig.add_subplot(111, polar=True)
sam = ['r','g','b']
lstype = ['-','--','-.']
lab = []
for i in range(len(kmeans_model.cluster_centers_)):
    values = kmeans_model.cluster_centers_[i]
    feature = ['R','F','M']
    values = np.concatenate((values, [values[0]]))
    # 绘制折线图
    ax.plot(angles, values, sam[i], linestyle=lstype[i], linewidth=2, markersize=10)
    ax.fill(angles, values, alpha=0.5)  # 填充颜色
    ax.set_thetagrids(angles * 180 / np.pi, feature, fontsize=15)  # 添加每个特征的标签
    plt.title('客户群特征分布图')  # 添加标题
    ax.grid(True)
    lab.append('客户群' + str(i+1))
plt.legend(lab)
plt.show()
plt.close
