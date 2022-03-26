# 代码 2-1
import numpy as np

print('整数42转换为浮点数的结果为：', np.float64(42))

print('浮点数42.0转换为整数的结果为：', np.int8(42.0))

print('浮点数42转换为布尔型的结果为：', np.bool(42.0))

print('整数0转换为布尔型的结果为：', np.bool(0))

print('布尔型数据True转换为浮点数的结果为：', np.float(True))

print('布尔型数据False转换为整型的结果为：', np.int8(False))

# 代码 2-2
arr1 = np.array([1, 2, 3, 4])
print('创建的一维ndarray为：', arr1)

arr2 = np.array([[1, 2, 3, 4], [4, 5, 6, 7], [7, 8, 9, 10]])
print('创建的二维ndarray为：\n', arr2)

# 代码 2-3
print('ndarray arr2的维数为：', arr2.ndim)

print('ndarray arr2的形状为：', arr2.shape)

print('ndarray arr2的数据类型为：', arr2.dtype)

print('ndarray arr2的元素个数为：', arr2.size)

print('ndarray arr2每个元素的大小为：', arr2.itemsize)

# 代码 2-4
print('使用arange函数创建的ndarray为：\n', np.arange(0, 1, 0.1))

# 代码 2-5
print('使用linspace函数创建的ndarray为：\n', np.linspace(0, 1, 12))

# 代码 2-6
print('使用logspace函数创建的ndarray为：\n', np.logspace(0, 2, 20))

# 代码 2-7
print('使用zeros函数创建的ndarray为：\n', np.zeros((2, 3)))

# 代码 2-8
print('使用eye函数创建的ndarray为：\n ', np.eye(3))  # 单位矩阵

# 代码 2-9
print('使用diag函数创建的ndarray为：\n', np.diag([1, 2, 3, 4]))  # 对角矩阵

# 代码 2-10
print('使用ones函数的ndarray为：\n', np.ones((2, 3)))

# 代码 2-11
print('random函数生成的随机数ndarray为：\n', np.random.random(100))

# 代码 2-12
print('rand函数生成的服从均匀分布的随机数ndarray为：\n', np.random.rand(4, 5))

# 代码 2-13
print('randint函数生成的指定上下限的随机整数ndarray为：\n',
      np.random.randint(low=2, high=10, size=[2, 5]))

# 代码 2-14
arr = np.arange(10)
print('使用元素位置索引结果为：', arr[5])

print('使用元素位置切片结果为：', arr[3:5])

print('省略单个位置切片结果为：', arr[:5])

print('使用元素反向位置切片结果为：', arr[:-1])

arr[2:4] = 100, 101  # 修改对应下标的值
print('修改后的ndarrayarr为：', arr)

print('元素位置等差索引结果为：', arr[1:-1:2])

# 步长为负数时，开始位置必须大于结束位置
print('元素位置负数步长等差索引结果为：', arr[5:1:-2])

# 代码 2-15
arr = np.array([[1, 2, 3, 4, 5], [4, 5, 6, 7, 8], [7, 8, 9, 10, 11]])
print('创建的二维ndarray arr为：\n', arr)

print('切片结果为：', arr[0, 3:5])  # 访问第0行中第3和第4列的元素

print('切片结果为：\n', arr[1:, 2:])  # 访问第1和第2行中第2列、第3列和第4列的元素

print('切片结果为：\n', arr[:, 2])  # 访问第3列所有的元素

# 代码 2-16
# 索引第1、3行中第2列的元素
mask = np.array([1, 0, 1], dtype=np.bool)
print('使用布尔值ndarray索引结果为：', arr[mask, 2])

# 代码 2-17
arr = np.empty((8, 4))
for i in range(8):
    arr[i] = i
print('创建的二维ndarray arr为：\n', arr)

print('以特定顺序索引arr结果为：\n', arr[[4, 3, 0, 6]])

print('以特定逆序索引arr结果为：\n', arr[[-3, -5, -7]])

# 代码 2-18
arr = np.array([np.arange(i * 4, i * 4 + 4) for i in np.arange(6)])
print('创建的二维ndarray arr为：\n', arr)

# 返回一个ndarray最终的元素(1,0)、(5,3)、(4,1)、(2,2)
print('使用二维ndarray索引arr结果为：', arr[[1, 5, 4, 2], [0, 3, 1, 2]])

# 代码 2-19
# 利用ix函数将两个一维的整数ndarray转化为方形区域的索引器
print('使用ix成片索引arr结果为：\n', arr[np.ix_([1, 5, 4, 2], [0, 3, 1, 2])])
