
###############################################################################
########################           第1题             ##########################
###############################################################################
from sklearn import preprocessing
import numpy as np

X = np.array([[1., -1.,  2.], 
              [2.,  0.,  0.], 
              [0.,  1., -1.]])

# 建立转换器并生成规则
SS_transformer = preprocessing.StandardScaler().fit(X)

print('标准差标准化后的数据为：\n', SS_transformer.transform(X))



###############################################################################
########################           第2题             ##########################
###############################################################################
# 使用多层感知机模型预测sklearn官方iris（鸢尾花）数据集类别
# 数据准备
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# 导入load_breast_cancer数据
iris = load_iris()
X = iris['data']
y = iris['target']

# 将数据划分为训练集测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=22)

# 数据标准化
from sklearn.preprocessing import StandardScaler
stdScaler = StandardScaler().fit(X_train)
X_trainStd = stdScaler.transform(X_train)
X_testStd = stdScaler.transform(X_test)

# 训练多层感知机模型
from sklearn.neural_network import MLPClassifier
MLP_model = MLPClassifier(max_iter=1000)
MLP_model.fit(X_trainStd, y_train)

# 预测
print('预测测试集前10个结果为：\n', MLP_model.predict(X_testStd)[:10])



###############################################################################
########################           第3题             ##########################
###############################################################################
# 使用决策树模型预测sklearn官方diabetes（糖尿病）数据集的目标值
# 数据准备
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split

# 导入load_breast_cancer数据
diabetes = load_diabetes()
X = diabetes['data']
y = diabetes['target']

# 将数据划分为训练集测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=22)

# 训练决策树模型
from sklearn.tree import DecisionTreeRegressor
DT_model = DecisionTreeRegressor()
DT_model.fit(X_train, y_train)

# 预测
print('预测测试集前10个结果为：\n', DT_model.predict(X_test)[:10])



###############################################################################
########################           第4题             ##########################
###############################################################################
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
# 导入load_breast_cancer数据
cancer = load_breast_cancer()
x = cancer.data
print('iris数据集前10行为：\n', x[: 10])
print('iris数据集的维度为：', x.shape)

from sklearn.decomposition import PCA
# 指定保留的特征数为20
pca = PCA(n_components=20).fit(x)
print('指定特征数的PCA模型为：\n', pca)
# 查看模型训练后各项特征的方差
print('各项特征的方差为：', pca.explained_variance_)
# 查看降维后的特征占所有特征的方差百分比
print('降维后的特征的方差占比为：', pca.explained_variance_ratio_)

# 指定降维后保留的方差百分比0.95
pca1 = PCA(n_components=0.95).fit(x)
print('指定方差百分比的PCA模型为：\n', pca1)

# 查看模型训练后各项特征的方差
print('各项特征的方差为：', pca.explained_variance_)
# 查看降维后的特征占所有特征的方差百分比
print('降维后的特征的方差占比为：', pca.explained_variance_ratio_)



###############################################################################
########################           第5题             ##########################
###############################################################################
from sklearn import datasets
from sklearn.cluster import KMeans
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt
# 导入数据
iris = datasets.load_iris()
x = iris.data
y = iris.target
plt.scatter(x[:, 0], x[:, 1], c=y)
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.title('原始数据', size=17)
plt.show()

# 生成DBSCAN模型，使用默认参数
ds_pre = DBSCAN().fit_predict(x)
plt.scatter(x[:, 0], x[:, 1], c=ds_pre)
plt.title('DBSCAN', size=17)
plt.show()

# K-means聚类
km_pre = KMeans(n_clusters=3, random_state=9).fit_predict(x)
plt.scatter(x[:, 0], x[:, 1], c=km_pre)
plt.title('K-means', size=17)
plt.show()



###############################################################################
########################           第6题             ##########################
###############################################################################
from sklearn import datasets
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
# 导入数据
iris = datasets.load_iris()
x = iris.data
y = iris.target
# 按7:3的比例划分数据集
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.3, random_state=0)
print('训练集维数为：', x_train.shape, '\n', '训练集样本个数为：', y_train.shape)

# 数据标准化
stdScaler = StandardScaler().fit(x_train)
x_trainStd = stdScaler.transform(x_train)
x_testStd = stdScaler.transform(x_test)
# SVM训练
from sklearn.svm import SVC
svc_model = SVC()
svc_model.fit(x_trainStd, y_train)
print('训练出来的SVM模型为：\n', svc_model)
print('预测测试集结果为：\n', svc_model.predict(x_testStd))
