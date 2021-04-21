# 代码 6-57
from sklearn import datasets
from sklearn.cluster import KMeans
# 导入数据
iris = datasets.load_iris()
x = iris.data
y = iris.target
# 构建并训练K-means模型
kmeans = KMeans(n_clusters=3, random_state=0).fit(x)
print('K-means模型为：\n', kmeans)



# 代码 6-58
print('簇的质心为：\n', kmeans.cluster_centers_)

print('样本所属的簇为：\n', kmeans.labels_)

print('样本到类中心的距离之和为：', kmeans.inertia_)



# 代码 6-59
import matplotlib.pyplot as plt
# 获取模型聚类结果
y_pre = kmeans.predict(x)
# 绘制iris原本的类别
plt.scatter(x[:, 0], x[:, 1], c=y)
plt.show()

# 绘制kmeans聚类结果
plt.scatter(x[:, 0], x[:, 1], c=y_pre)
plt.show()



# 代码 6-60
from sklearn.cluster import AgglomerativeClustering
# 单链接层次聚类
clusing_ward = AgglomerativeClustering(n_clusters=3).fit(x)
print('单链接层次聚类模型为：\n', clusing_ward)



# 代码 6-61
print('簇类别标签为：\n', clusing_ward.labels_)

print('叶节点数量为：', clusing_ward.n_leaves_)



# 代码 6-62
# 绘制单链接聚类结果
cw_ypre = AgglomerativeClustering(n_clusters=3).fit_predict(x)
plt.scatter(x[:, 0], x[:, 1], c=cw_ypre)
plt.rcParams['font.sans-serif'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False
plt.title('单链接聚类', size=17)
plt.show()

# 绘制均链接聚类结果
cw_ypre = AgglomerativeClustering(linkage='average',
                                  n_clusters=3).fit_predict(x)
plt.scatter(x[:, 0], x[:, 1], c=cw_ypre)
plt.title('均链接聚类', size=17)
plt.show()

# 绘制全链接聚类结果
cw_ypre = AgglomerativeClustering(linkage='complete', n_clusters=3).fit_predict(x)
plt.scatter(x[:, 0], x[:, 1], c=cw_ypre)
plt.title('全链接聚类', size=17)
plt.show()



# 代码 6-63
import numpy as np
from sklearn.cluster import DBSCAN
# 生成两簇非凸数据
x1, y2 = datasets.make_blobs(n_samples=1000, n_features=2,
                             centers=[[1.2, 1.2]], cluster_std=[[.1]],
                             random_state=9)
# 一簇对比数据
x2, y1 = datasets.make_circles(n_samples=5000, factor=.6, noise=.05)
x = np.concatenate((x1, x2))
plt.scatter(x[:, 0], x[:, 1], marker='o')
plt.show()

# 生成DBSCAN模型，使用默认参数
dbs = DBSCAN().fit(x)
print('默认参数的DBSCAN模型:\n', dbs)



# 代码 6-64
print('DBSCAN模型的簇标签为：', dbs.labels_)

print('核心样本的位置为：', dbs.core_sample_indices_)



# 代码 6-65
# 调整eps参数和min_samples参数
ds_pre = DBSCAN(eps=0.1, min_samples=12).fit_predict(x)
plt.scatter(x[:, 0], x[:, 1], c=ds_pre)
plt.title('DBSCAN', size=17)
plt.show()

# K-means聚类
km_pre = KMeans(n_clusters=3, random_state=9).fit_predict(x)
plt.scatter(x[:, 0], x[:, 1], c=km_pre)
plt.title('K-means', size=17)
plt.show()



# 代码 6-66
# 导入数据
iris = datasets.load_iris()
x = iris.data
y = iris.target
# 绘制样本数据
plt.scatter(x[:, 0], x[:, 1], c=y)
plt.title('iris', size=17)
plt.show()

# 构建聚类数为3的GMM模型
from sklearn.mixture import GaussianMixture
gmm = GaussianMixture(n_components=3).fit(x)
print('GMM模型：\n', gmm)



# 代码 6-67
print('GMM模型的权重为：', gmm.weights_)

print('GMM模型的均值为：\n', gmm.means_)



# 代码 6-68
# 获取GMM模型聚类结果
gmm_pre = gmm.predict(x)
plt.scatter(x[:, 0], x[:, 1], c=gmm_pre)
plt.title('GMM', size=17)
plt.show()



# K-means聚类
km_pre = KMeans(n_clusters=3).fit_predict(x)
plt.scatter(x[:, 0], x[:, 1], c=km_pre)
plt.title('K-means', size=17)
plt.show()
