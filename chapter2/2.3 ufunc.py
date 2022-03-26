# 代码 2-39
import numpy as np

arr1 = np.array([[0, 0, 0], [1, 1, 1], [2, 2, 2], [3, 3, 3]])
print('创建的ndarray arr1为：\n', arr1)

arr2 = np.array([1, 2, 3])
print('创建的ndarray arr2为：', arr2)

print('arr1与arr2相加结果为：\n', arr1 + arr2)

# 代码 2-40
arr3 = np.arange(1, 5).reshape(4, 1)
print('创建的ndarray arr3为：\n', arr3)

print('arr1与arr3相加结果为：\n', arr1 + arr3)

# 代码 2-41
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
print('ndarray arr1，arr2相加结果为：', arr1 + arr2)

print('ndarray arr1，arr2相减结果为：', arr1 - arr2)

print('ndarray arr1，arr2相乘结果为：', arr1 * arr2)

print('ndarray arr1，arr2相除结果为：', arr1 / arr2)

print('ndarray arr1，arr2幂运算结果为：', arr1 ** arr2)

# 代码 2-42
arr = np.arange(-4, 5).reshape(3, 3)
print('创建的ndarray arr为：\n', arr)

print('ndarray arr各元素的相反数为：\n', np.negative(arr))

print('ndarray arr各元素的绝对值为：\n', np.absolute(arr))

print('ndarray arr各元素的符号为：\n', np.sign(arr))

print('ndarray arr各元素的平方根为：\n', np.sqrt(arr))

print('ndarray arr各元素的自然对数为：\n', np.log1p(arr))

# 代码 2-43
rad = np.array([0, np.pi * 1 / 6, np.pi * 1 / 4, np.pi * 1 * 3, np.pi * 1 / 2])
print('将弧度制ndarray rad转换为角度制后为：', np.rad2deg(rad))

print('ndarray rad各元素的正切为：\n ', np.tan(rad))

print('ndarray rad各元素的正弦为：\n ', np.sin(rad))

print('ndarray rad各元素的余弦为：\n ', np.cos(rad))

arr = np.array([0, 1 / 2, np.sqrt(2) / 2, np.sqrt(3) / 2, 1])
print('ndarray arr各元素的三角反正弦为：\n ', np.arcsin(arr))

print('通过直角边3，4求出的斜边为：\n', np.hypot(3, 4))

# 代码 2-44
arr1 = np.arange(-4, 5)
print('创建的ndarray arr1为：', arr1)

arr2 = np.arange(9)
print('创建的ndarray arr2为：', arr2)

print('ndarray arr1与arr2的交集为：', np.intersect1d(arr1, arr2))

print('ndarray arr1与arr2的并集为：', np.union1d(arr1, arr2))

print('ndarray arr1与arr2的差集为：', np.setdiff1d(arr1, arr2))

print('ndarray arr1与arr2的对称差集为：', np.setxor1d(arr1, arr2))

# 代码 2-45
arr1 = np.array([1, 3, 5])
arr2 = np.array([2, 3, 4])
print('ndarray x等于y的比较结果为：', arr1 == arr2, np.equal(arr1, arr2))

print('ndarray x不等于y的比较结果为：', arr1 != arr2, np.not_equal(arr1, arr2))

print('ndarray x小于y的比较结果为：', arr1 < arr2, np.less(arr1, arr2))

print('ndarray x大于y的比较结果为：', arr1 > arr2, np.greater(arr1, arr2))

# 代码 2-46
arr1 = [True, True, False, False, False]
print('创建的ndarray arr1为：', arr1)

arr2 = [True, False, True, False, True]
print('创建的ndarray arr2为：', arr2)

print('ndarray arr1与arr2的逻辑与运算结果为：', np.logical_and(arr1, arr2))

print('ndarray arr1与arr2的逻辑或运算结果为：', np.logical_or(arr1, arr2))

print('ndarray arr1的逻辑非运算结果为：', np.logical_not(arr1))

print('ndarray arr1与arr2的逻辑异或运算结果为：', np.logical_xor(arr1, arr2))

# 代码 2-47
arr = np.arange(20).reshape(4, 5)
print('创建的ndarray arr为：\n', arr)

print('ndarray arr各元素的和为：', np.sum(arr))

print('ndarray arr各行的极差为：', np.ptp(arr, axis=1))

print('ndarray arr各列的均值为：', np.mean(arr, axis=0))

print('ndarray arr的中位数为：', np.median(arr))

print('ndarray arr各行的上四分位数为：', np.percentile(arr, 75, axis=1))

print('ndarray arr各列的下四分位数为：', np.percentile(arr, 25, axis=0))

print('ndarray arr的标准差为：', np.std(arr))

print('ndarray arr的方差为：', np.var(arr))

print('ndarray arr的最小值为：', np.min(arr))

print('ndarray arr的最大值为：', np.max(arr))

# 代码 2-48
arr = np.arange(1, 11)
print('创建的ndarray arr为：', arr)

print('ndarray arr的元素累计和为：', np.cumsum(arr))

print('ndarray arr的元素累计积为：\n', np.cumprod(arr))
