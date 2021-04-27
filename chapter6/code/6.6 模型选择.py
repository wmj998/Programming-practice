# 代码 6-69
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_breast_cancer
cancer = load_breast_cancer()
x = cancer['data']
y = cancer['target']
print('cancer数据集维数为：', x.shape, '\n', 'cancer样本个数为：', y.shape)

# 按7:3的比例划分数据集
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.3, random_state=0)
print('训练集维数为：', x_train.shape, '\n', '训练集样本个数为：', y_train.shape)

print('测试集维数为：', x_test.shape, '\n', '测试集样本个数为：', y_test.shape)



# 代码 6-70
# 对svm模型进行交叉验证
from sklearn import svm
from sklearn.model_selection import cross_val_score
clf = svm.SVC(kernel='linear', C=1)
score = cross_val_score(clf, cancer.data, cancer.target, cv=5)
print('交叉验证结果为：\n', score)



# 代码 6-71
from sklearn.model_selection import GridSearchCV
from sklearn.decomposition import PCA
# 构建PCA模型
pca = PCA(n_components=2)
# 设置要调整的参数
param_grid = {'n_components': [1, 2, 3]}
# 设置自动调参容器
grid_search = GridSearchCV(pca, param_grid=param_grid).fit(x, y)
print('自动调参容器为：\n', grid_search)


# 代码 6-72
print('最佳结果参数设置为：', grid_search.best_params_)



# 代码 6-73
from sklearn.svm import SVC
SVC_model = SVC()
SVC_model.fit(x_train, y_train)
y_pred = SVC_model.predict(x_test)
# 准确率
from sklearn.metrics import accuracy_score
print('准确率为：', accuracy_score(y_true=y_test, y_pred=y_pred))

# 混淆矩阵
from sklearn.metrics import classification_report
print('混淆矩阵为：\n', classification_report(y_true=y_test, y_pred=y_pred))

# ROC曲线
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, auc
fpr, tpr, thresholds = roc_curve(y_test, y_pred)
roc_auc = auc(fpr, tpr)
plt.plot(fpr, tpr, lw=1, label='ROC(area = %0.2f)' %(roc_auc))
plt.rcParams['font.sans-serif'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False
plt.xlabel("FPR (假正率)")
plt.ylabel("TPR (真正率)")
plt.title("ROC曲线, ROC(AUC = %0.2f)" %(roc_auc))
plt.legend()
plt.show()



# 代码 6-74
# 均方差
from sklearn.metrics import mean_squared_error
print('均方误差为：', mean_squared_error(y_true=y_test, y_pred=y_pred))

# 平均绝对误差
from sklearn.metrics import mean_absolute_error
print('平均绝对误差为：', mean_absolute_error(y_true=y_test, y_pred=y_pred))

# 中值绝对误差
from sklearn.metrics import median_absolute_error
print('中值绝对误差为：', median_absolute_error(y_true=y_test, y_pred=y_pred))

from sklearn.metrics import r2_score
print('R2决定系数为：', r2_score(y_true=y_test, y_pred=y_pred))



# 代码 6-75
from sklearn.cluster import KMeans
# 使用K-means聚类
km = KMeans(n_clusters=2, random_state=0).fit(x)
# 轮廓系数
from sklearn.metrics import silhouette_score
print('轮廓系数为：', silhouette_score(x, km.labels_, metric='euclidean'))

# 同质性、完整性、调和平均
from sklearn.metrics import homogeneity_completeness_v_measure
km_pred = km.predict(x)
print('同质性,完整性,调和平均分别为：\n',
      homogeneity_completeness_v_measure(y, km_pred))
