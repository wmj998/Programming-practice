# 代码 6-46
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
# 导入load_boston数据
boston = load_boston()
x = boston['data']
y = boston['target']
names = boston['feature_names']
# 将数据划分为训练集和测试集
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2,
                                                    random_state=22)
print('x_train前3行数据为：', x_train[0: 3], '\n',
      'y_train前3个数据为：', y_train[0: 3])



# 代码 6-47
# 使用LinearRegression类构建线性回归模型
from sklearn.linear_model import LinearRegression
lr_model = LinearRegression()
# 训练模型
lr_model.fit(x_train, y_train)
print('训练出来的LinearRegression模型为：\n', lr_model)



# 代码 6-48
print('LinearRegression模型中各特征系数为：\n', lr_model.coef_)

print('LinearRegression模型中截距为：', lr_model.intercept_)



# 代码 6-49
print('预测测试集前5个结果为：\n', lr_model.predict(x_test)[: 5])

print('测试集R2值为：', lr_model.score(x_test, y_test))



# 代码 6-50
import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams['font.sans-serif'] = 'SimHei'
fig = plt.figure(figsize=(10, 6))
y_pred = lr_model.predict(x_test)
plt.plot(range(y_test.shape[0]), y_test, color="blue",
         linewidth=1.5, linestyle="-")
plt.plot(range(y_test.shape[0]), y_pred, color="red",
         linewidth=1.5, linestyle="-.")
plt.legend(['真实值', '预测值'])
plt.show()



# 代码 6-51
from sklearn.linear_model import Ridge
ridge_model = Ridge()
ridge_model.fit(x_train, y_train)
print('训练出来的ridge模型为：\n', ridge_model)



# 代码 6-52
print('迭代次数为：', ridge_model.n_iter_)



# 代码 6-53
print('预测测试集前5个结果为：\n', ridge_model.predict(x_test)[: 5])

print('测试集R^2值为：', ridge_model.score(x_test, y_test))



# 代码 6-54
from sklearn.linear_model import Lasso
lasso_model = Lasso()
lasso_model.fit(x_train, y_train)
print('训练出来的Lasso模型为：\n', lasso_model)



# 代码 6-55
print('scipy.sparse matrix为：\n', lasso_model.sparse_coef_)



# 代码 6-56
print('预测测试集前5个结果为：\n', lasso_model.predict(x_test)[: 5])

print('测试集R2值为：', lasso_model.score(x_test, y_test))

print('测试集弹性网络路径为：\n', lasso_model.path(x_test, y_test))
