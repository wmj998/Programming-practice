import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.linear_model import Perceptron
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

# 读取数据
train_2 = pd.read_excel('../data/train_2.xlsx')
test_2 = pd.read_excel('../data/test_2.xlsx')

# 选取训练集及对应测试集，
# 第一种是直接对应columns选取

train_x = train_2[['Sex', 'Length', 'Diameter', 'Height', 'Whole weight', 'Shucked weight', 'Viscera weight', 'Shell weight']]
train_y = train_2['Rings']
test_x = test_2[['Sex', 'Length', 'Diameter', 'Height', 'Whole weight', 'Shucked weight', 'Viscera weight', 'Shell weight']]

# 第二种是使用drop进行删除不想选取的columns
# train_x = train_2.drop(columns=['Rings'])
# train_y = train_2['Rings']
# test_x = test_2.drop(columns=['Rings'])


# x_train = np.array(train_x)
# y_train = np.array(train_y)
# x_test = np.array(test_x)

x_train = train_x.values
y_train = train_y.values
x_test = test_x.values

# knn拟合预测
# knn = KNeighborsClassifier(n_neighbors=6)
# knn.fit(x_train, y_train)
# y_test = knn.predict(x_test)

# svc拟合预测
# svc = SVC(kernel='rbf', probability=True)
# svc.fit(x_train, y_train)
# y_test = svc.predict(x_test)

# 感知器分类
# ppn = Perceptron()
# ppn.fit(x_train, y_train)
# y_test = ppn.predict(x_test)

# logistic分类
# lr = LogisticRegression(C=1000.0, random_state=0)
# lr.fit(x_train, y_train)
# y_test = lr.predict(x_test)

# 决策树分类
# tree = DecisionTreeClassifier(criterion='entropy', max_depth=3, random_state=0)
# tree.fit(x_train, y_train)
# y_test = tree.predict(x_test)

# 随机森林分类
forest = RandomForestClassifier(criterion='entropy', n_estimators=10, random_state=1, n_jobs=2)
forest.fit(x_train, y_train)
y_test = forest.predict(x_test)

# 输出数据到test表格中
test_2['label'] = y_test
test_2.to_excel('../temp/test_2.xlsx', index=False)
