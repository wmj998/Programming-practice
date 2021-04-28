# 代码 6-13
from sklearn import datasets
# 加载iris数据集
iris = datasets.load_iris()
x = iris.data
print('iris数据集前10行为：\n', x[: 10])

print('iris数据集的维度为：', x.shape)



# 代码 6-14
from sklearn.decomposition import PCA
# 指定保留的特征数为3
pca = PCA(n_components=3).fit(x)
print('指定特征数的PCA模型为：\n', pca)
# 指定降维后保留的方差百分比0.95
pca1 = PCA(n_components=0.95).fit(x)
print('指定方差百分比的PCA模型为：\n', pca1)

# 指定使用MLE最大似然算法自动降维
pca2 = PCA(n_components="mle").fit(x)
print('指定MLE算法的PCA模型为：\n', pca2)



# 代码 6-15
# 查看模型训练后各项特征的方差
print('各项特征的方差为：', pca.explained_variance_)

# 查看降维后的特征占所有特征的方差百分比
print('降维后的特征的方差占比为：', pca.explained_variance_ratio_)



# 代码 6-16
# 查看指定特征数的结果
x_pca = pca.transform(x)
print('指定特征数的降维结果前10行数据为：\n', x_pca[: 10])

# 查看指定方差百分比的降维结果
x_pca1 = pca1.transform(x)
print('指定方差百分比的降维结果前10行数据为：\n', x_pca1[: 10])

# 查看MLE算法降维结果
x_pca2 = pca2.transform(x)
print('MLE算法的降维结果前10行数据为：\n', x_pca2[: 10])



# 代码 6-17
import numpy as np
from scipy import signal
# 数据准备
np.random.seed(0)
n_samples = 2000
time = np.linspace(0, 8, n_samples)
# 生成3种源信号
waft1 = np.sin(2 * time)  # 正弦信号
waft2 = np.sign(np.sin(3 * time))  # 方波信号
waft3 = signal.sawtooth(2 * np.pi * time)  # 锯齿信号
print('正弦信号为：\n', waft1, '\n',
      '方波信号为：\n', waft2, '\n',
      '锯齿信号为：\n', waft3)

# 生成混淆信号
waft = np.c_[waft1, waft2, waft3]
waft += 0.2 * np.random.normal(size=waft.shape)  # 增加噪声
waft /= waft.std(axis=0)  # 数据标准化
arr = np.array([[1, 1, 1], [0.5, 2, 1.0], [1.5, 1.0, 2.0]])  # 混淆矩阵
mix_waft = np.dot(waft, arr.T)  # 生成的混淆信号
print('混淆信号为：\n', mix_waft)



# 代码 6-18
from sklearn.decomposition import FastICA
ica = FastICA(n_components=3).fit(mix_waft)
print('ICA模型为：\n', ica)



# 代码 6-19
ica_mixing = ica.mixing_
print('ICA使用的混淆矩阵：\n', ica_mixing)



# 代码 6-20
import matplotlib.pyplot as plt
# 使用ICA还原信号
waft_ica = ica.transform(mix_waft)
# 使用PCA还原信号
waft_pca = PCA(n_components=3).fit_transform(mix_waft)
# 绘制结果
plt.figure(figsize=[12, 6])  # 设置画布大小
# 设置中文显示
plt.rcParams['font.sans-serif'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False
models = [mix_waft, waft, waft_ica, waft_pca]
names = ['混淆信号',
         '实际源信号',
         'ICA复原信号',
         'PCA复原信号']
colors = ['red', 'steelblue', 'orange']
for i, (model, name) in enumerate(zip(models, names), 1):
    plt.subplot(4, 1, i)
    plt.title(name)
    for sig, color in zip(model.T, colors):
        plt.plot(sig, color=color)
plt.subplots_adjust(0.09, 0.04, 0.94, 0.94, 0.26, 0.46)
plt.show()



# 代码 6-21
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
y = iris.target
# 构建并训练LDA模型
lda = LinearDiscriminantAnalysis(n_components=2).fit(x,y)
print('LDA模型为：\n', lda)

# 构建并训练PCA模型
pca = PCA(n_components=2).fit(x)
print('PCA模型为：\n', pca)



# 代码 6-22
print('LDA模型方差百分比为：', lda.explained_variance_ratio_)

print('LDA模型类标签为：', lda.classes_)



# 代码 6-23
target_names = iris.target_names
# 获取LDA与PCA模型的降维结果
x_lda = lda.transform(x)
x_pca = pca.transform(x)
# 绘制图形进行效果对比
plt.figure()
# 设置中文显示
plt.rcParams['font.sans-serif'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False
colors = ['navy', 'turquoise', 'darkorange']
markers = ['*','.','d']
lw = 2
for color, i, target_name, marker in zip(colors, [0, 1, 2], 
                                         target_names, markers):
    plt.scatter(x_pca[y == i, 0], x_pca[y == i, 1], color=color, 
                alpha=.8, lw=lw, label=target_name,
                marker=marker)
plt.legend(loc='best', shadow=False, scatterpoints=1)
plt.title('PCA降维结果')
plt.figure()
for color, i, target_name, marker in zip(colors, [0, 1, 2], 
                                         target_names, markers):
    plt.scatter(x_lda[y == i, 0], x_lda[y == i, 1], 
                alpha=.8, color=color, label=target_name,
                marker=marker)
plt.legend(loc='best', shadow=False, scatterpoints=1)
plt.title('LDA降维结果')
plt.show()
