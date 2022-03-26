# 代码 2-20
import numpy as np

arr = np.arange(12)  # 创建一维ndarray
print('创建的一维ndarray arr为：', arr)

arr1 = arr.reshape(3, 4)  # 设置ndarray的维度
print('改变形状后的ndarray arr1为：\n', arr1)

print('形状改变后ndarray arr1的维度为：', arr1.ndim)

# 代码 2-21
arr.resize(2, 6)
print('resize改变原ndarray形状，ndarray arr变为：\n', arr)

# 代码 2-22
arr.shape = (4, 3)
print('通过重新设置shape属性后，ndarray arr为：\n', arr)

# 代码 2-23
arr = np.arange(12).reshape(3, 4)
print('创建的二维ndarray arr为：\n', arr)

print('ndarray arr横向展平后为：', arr.ravel())

# 代码 2-24
print('ndarray arr使用flatten方法横向展平后为：', arr.flatten())

print('ndarray arr使用flatten方法纵向展平后为：', arr.flatten('F'))

# 代码 2-25
arr1 = np.arange(12).reshape(3, 4)
print('创建的ndarray arr1为：\n', arr1)

arr2 = arr1 * 3
print('创建的ndarray arr2为：\n', arr2)

print('hstack横向组合ndarray arr1与arr2为：\n', np.hstack((arr1, arr2)))

# 代码 2-26
print('vstack纵向组合ndarray arr1与arr2为：\n', np.vstack((arr1, arr2)))

# 代码 2-27
print('concatenate横向组合arr1与arr2为：\n', np.concatenate((arr1, arr2), axis=1))

print('concatenate纵向组合arr1与arr2为：\n', np.concatenate((arr1, arr2), axis=0))

# 代码 2-28
print('dstack深度组合arr1与arr2为：\n', np.dstack((arr1, arr2)))

arr3 = []
for x, y in list(zip(arr1, arr2)):
    arr3.append(list(zip(x, y)))
arr3 = np.array(arr3)
print('zip函数实现深度合并的arr3与dstack实现的等价：\n',
      arr3 == np.dstack((arr1, arr2)))

# 代码 2-29
arr = np.arange(16).reshape(4, 4)
print('创建的二维ndarray arr为：\n', arr)

print('hsplit横向分割arr为：\n', np.hsplit(arr, 2))

# 代码 2-30
print('hsplit纵向分割arr为：\n', np.vsplit(arr, 2))

# 代码 2-31
print('split横向分割arr为：\n', np.split(arr, 2, axis=1))

print('split纵向分割arr为：\n', np.split(arr, 2, axis=0))

# 代码 2-32
arr = np.arange(12).reshape(2, 2, 3)
print('创建的三维ndarray arr为：\n', arr)

print('dsplit深度分割arr为：\n', np.dsplit(arr, 3))

# 代码 2-33
np.random.seed(42)  # 设置随机种子
arr = np.random.randint(1, 10, size=12).reshape(4, 3)
print('创建的随机数ndarray arr为：\n', arr)

print('默认排序后ndarray arr为：\n', np.sort(arr))

print('展平排序的ndarray arr为：', np.sort(arr, axis=None))

print('横轴排序后ndarray arr为：\n', np.sort(arr, axis=1))

print('纵轴排序后ndarray arr为：\n', np.sort(arr, axis=0))

# 代码 2-34
print('横轴排序后arr的下标为：\n', np.argsort(arr, axis=1))

print('展平排序后arr的下标为：', np.argsort(arr, axis=None))

# 代码 2-35
arr = np.arange(6, 12).reshape(2, 3)
print('创建的ndarray arr为：\n', arr)

print('ndarray arr中最大元素的索引为：', np.argmax(arr))
print('ndarray arr中最小元素的索引为：', np.argmin(arr))

print('ndarray arr中各列最大元素的索引为：', np.argmax(arr, axis=0))
print('ndarray arr中各行最小元素的索引为：', np.argmin(arr, axis=1))

# 代码 2-36
arr = np.arange(12).reshape(4, 3)
print('创建的ndarray arr为：\n', arr)

print('where输出ndarray arr满足条件的下标为：\n', np.where(arr > 6))

# 代码 2-37
arr1 = np.arange(12).reshape(3, 4)
print('创建的ndarray arr1为：\n', arr1)

arr2 = np.arange(-12, 0).reshape(3, 4)
print('创建的ndarray arr2为：\n', arr2)

exp = arr1 > 5
print('arr1大于5的布尔ndarray为：\n', exp)

print('where函数搜索符合条件的arr1与arr2为：\n', np.where(exp, arr1, arr2))

# 代码 2-38
arr = np.arange(9).reshape(3, 3)
print('创建的ndarray arr为：\n', arr)

exp = (arr % 2) == 0
print('arr能被2整除的布尔ndarray为：\n', exp)

print('arr基于条件exp提取的元素为：\n', np.extract(exp, arr))
