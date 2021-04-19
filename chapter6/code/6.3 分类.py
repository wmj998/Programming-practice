# 代码 6-24
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
# 导入load_breast_cancer数据
cancer = load_breast_cancer()
x = cancer['data']
y = cancer['target']
# 将数据划分为训练集测试集
x_train, x_test, y_train, y_test = train_test_split(x, y, 
        test_size=0.2, random_state=22)
print('x_train第1行数据为：\n', x_train[0: 1], '\n', 'y_train第1个数据为：', y_train[0: 1])



# 代码 6-25
# 数据标准化
from sklearn.preprocessing import StandardScaler
stdScaler = StandardScaler().fit(x_train)
x_trainStd = stdScaler.transform(x_train)
x_testStd = stdScaler.transform(x_test)



# 使用LogisticRegression类构建Logistic回归模型
from sklearn.linear_model import LogisticRegression
lr_model = LogisticRegression(solver='saga')
# 训练Logistic回归模型
lr_model.fit(x_trainStd, y_train)
print('训练出来的LogisticRegression模型为：\n', lr_model)



# 代码 6-26
print('各特征的相关系数为：\n', lr_model.coef_)

print('模型的截距为：', lr_model.intercept_)

print('模型的迭代次数为：', lr_model.n_iter_)



# 代码 6-27
print('预测测试集前10个结果为：\n', lr_model.predict(x_testStd)[: 10])

print('测试集准确率为：', lr_model.score(x_testStd, y_test))

print('测试集前3个对应类别的概率为：\n', lr_model.predict_proba(x_testStd)[: 3])

print('测试集前3个对应类别的概率的log值为：\n',
      lr_model.predict_log_proba(x_testStd)[: 3])

print('测试集前3个的决策函数值为：\n',
      lr_model.decision_function(x_testStd)[: 3])

print('模型的参数为：\n', lr_model.get_params())

print('修改max_iter参数为1000后的模型为：\n', lr_model.set_params(max_iter=1000))

print('系数矩阵转为密度数组后的模型为：\n', lr_model.densify())

print('系数矩阵转为稀疏形式后的模型为：\n', lr_model.sparsify())



# 代码 6-28
from sklearn.svm import SVC
svc_model = SVC()
svc_model.fit(x_trainStd, y_train)
print('训练出来的SVM模型为：\n', svc_model)



# 代码 6-29
print('前5个支持向量的索引为：', svc_model.support_[0: 5])

print('第1个支持向量为：\n', svc_model.support_vectors_[0: 1])

print('每个类别支持向量的个数为：', svc_model.n_support_)

print('支持向量的系数为：\n', svc_model.dual_coef_)

print('模型的截距值为：', svc_model.intercept_)



# 代码 6-30
print('预测测试集前10个结果为：\n', svc_model.predict(x_testStd)[: 10])

print('测试集准确率为：', svc_model.score(x_testStd, y_test))

print('测试集前10个距超平面的距离为：\n', svc_model.decision_function(x_testStd)[: 10])



# 代码 6-31
from sklearn.tree import DecisionTreeClassifier
dt_model = DecisionTreeClassifier()
dt_model.fit(x_train, y_train)
print('训练出来的决策树模型为：\n', dt_model)



# 代码 6-32
# 决策过程可视化，需安装graphviz，结果输出为pdf文件
from sklearn import tree
import graphviz
dot_data = tree.export_graphviz(dt_model, out_file=None)
graph = graphviz.Source(dot_data)
graph.render("../tmp/cancer")



# 代码 6-33
print('决策树模型类别标签为：', dt_model.classes_)

print('每个特征的重要性数值为：\n', dt_model.feature_importances_)

print('最大特征数为：', dt_model.max_features_)

print('决策树模型的类别数为：', dt_model.n_classes_)

print('决策树模型的特征数为：', dt_model.n_features_)

print('决策树模型的输出结果数量为：', dt_model.n_outputs_)



# 代码 6-34
print('预测测试集前10个结果为：\n', dt_model.predict(x_test)[: 10])

print('测试集准确率为：', dt_model.score(x_test, y_test))

print('测试集前5个叶节点索引为：', dt_model.apply(x_test)[0: 5])

print('测试集前2个决策路径为：\n', dt_model.decision_path(x_test)[0: 2])



# 代码 6-35
# 使用KNeighborsClassifier类构建knn模型
from sklearn.neighbors import KNeighborsClassifier
knn_model = KNeighborsClassifier()
knn_model.fit(x_trainStd, y_train)
print('训练出来的knn模型为：\n', knn_model)



# 代码 6-36
print('预测测试集前10个结果为：\n', knn_model.predict(x_testStd)[: 10])

print('测试集准确率为：', knn_model.score(x_testStd, y_test))

print('测试集前5个最近邻点为：\n',
      knn_model.kneighbors(x_testStd)[0][0: 5], '\n',
      '测试集前5个最近邻点的距离为：\n',
      knn_model.kneighbors(x_testStd)[1][0: 5])

mat = knn_model.kneighbors_graph(x_testStd)
print('将CSR格式的稀疏矩阵显示的最近邻点转换为数组后结果为：\n', mat.toarray())



# 代码 6-37
# 使用GaussianNB类构建朴素贝叶斯模型
from sklearn.naive_bayes import GaussianNB
gnb_model = GaussianNB()
gnb_model.fit(x_train, y_train)
print('训练出来的朴素贝叶斯模型为：', gnb_model)



# 代码 6-38
print('每个类别出现的概率为：', gnb_model.class_prior_)

print('每个类别训练样本的数量为：', gnb_model.class_count_)

print('每个类别中每个特征的均值为：\n', gnb_model.theta_)

print('每个类别中每个特征的方差为：\n', gnb_model.sigma_)



# 代码 6-39
print('预测测试集前10个结果为：\n', gnb_model.predict(x_test)[: 10])

print('测试集准确率为：', gnb_model.score(x_test, y_test))

print('追加训练数据后的模型为：', gnb_model.partial_fit(x_test, y_test))



# 代码 6-40
# 使用RandomForestClassifier类构建随机森林分类模型
from sklearn.ensemble import RandomForestClassifier
rf_model = RandomForestClassifier()
rf_model.fit(x_train, y_train)
print('训练出来的随机森林模型为：\n', rf_model)



# 代码 6-41
print('训练出来的前2个决策树模型为：\n', rf_model.estimators_[0: 2])



# 代码 6-42
print('预测测试集前10个结果为：\n', rf_model.predict(x_test)[: 10])

print('测试集准确率为：', rf_model.score(x_test, y_test))



# 代码 6-43
from sklearn.neural_network import MLPClassifier
mlp_model = MLPClassifier(max_iter=1000, random_state=3)
mlp_model.fit(x_trainStd, y_train)
print('训练出来的多层感知机模型为：\n', mlp_model)



# 代码 6-44
print('分类模型的类别标签为：', mlp_model.classes_)

print('当前损失值为：', mlp_model.loss_)

print('迭代次数为：', mlp_model.n_iter_)

print('神经网络层数为：', mlp_model.n_layers_)

print('输出个数为：', mlp_model.n_outputs_)

print('输出激活函数的名称为：', mlp_model.out_activation_)

print('权重矩阵为：\n', mlp_model.coefs_)

print('偏差向量为：\n', mlp_model.intercepts_)

# 代码 6-45
print('预测测试集前10个结果为：\n', mlp_model.predict(x_testStd)[: 10])

print('测试集准确率为：', mlp_model.score(x_testStd, y_test))
