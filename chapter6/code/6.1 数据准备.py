# 代码 6-1
from sklearn import preprocessing
import numpy as np
x_train = np.array([[1., -1., 2.],
                    [2., 0., 0.],
                    [0., 1., -1.]])
x_test = np.array([[-1., 1., 0.]])
# 创建转换器并生成规则
std_transformer = preprocessing.StandardScaler().fit(x_train)
print('生成规则后的标准差标准化转换器为：\n', std_transformer)



# 代码 6-2
print('特征均值为：\n', std_transformer.mean_, '\n', '特征方差为：\n', std_transformer.var_)



# 代码 6-3
print('标准差标准化后的训练集为：\n', std_transformer.transform(x_train))

print('标准差标准化后的测试集为：\n', std_transformer.transform(x_test))



# 代码 6-4
# 创建转换器并生成规则
mms_transformer = preprocessing.MinMaxScaler().fit(x_train)
print('生成规则后的离差标准化转换器为：\n', mms_transformer)



# 代码 6-5
print('特征最大值为：', mms_transformer.data_max_)

print('特征最小值为：', mms_transformer.data_min_)


# 代码 6-6
print('离差标准化后的训练集为：\n', mms_transformer.transform(x_train))

print('离差标准化后的测试集为：\n', mms_transformer.transform(x_test))



# 代码 6-7
# 创建转换器并生成规则
norm_transformer = preprocessing.Normalizer().fit(x_train)
print('生成规则后的离差标准化转换器为：\n', norm_transformer)



# 代码 6-8
print('归一化后的训练集为：\n', norm_transformer.transform(x_train))

print('归一化后的测试集为：\n', norm_transformer.transform(x_test))



# 代码 6-9
# 创建转换器并生成规则
bin_transformer = preprocessing.Binarizer().fit(x_train)
print('生成规则后的二值化转换器为：\n', bin_transformer)



# 代码 6-10
print('二值化后的训练集为：\n', bin_transformer.transform(x_train))

print('二值化后的测试集为：\n', bin_transformer.transform(x_test))



# 代码 6-11
x_train = np.array([['男', '北京', '已婚'],
                    ['男', '上海', '未婚'],
                    ['女', '广州', '已婚']])
x_test = np.array([['男', '北京', '未婚']])
# 构建分类型转换为数值型函数


def auto_coder(X):
    for i in range(X.shape[1]):
        X[:, i] = preprocessing.LabelEncoder().fit_transform(X[:, i])
    X = X.astype(int)
    return X


# 将训练集转换为数值型
x_train_num = auto_coder(x_train)
print('转换为数值型后的训练集为：\n', x_train_num)

# 创建转换器并生成规则
oe_transformer = preprocessing.OneHotEncoder().fit(x_train_num)
print('生成规则后的独热编码转换器为：\n', oe_transformer)



# 代码 6-12
print('独热编码后的训练集为：\n',
      oe_transformer.transform(x_train_num).toarray())

x_test_num = auto_coder(x_test)
print('独热编码后的测试集为：\n',
      oe_transformer.transform(x_test_num).toarray())
