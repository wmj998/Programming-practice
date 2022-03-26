age = input('请输入您的年龄：')
age = int(age)
if age < 18:
    print('未成年人！')
elif age >= 18 and age <= 25:
    print('青年人！')
elif age > 25 and age <= 60:
    print('中年人！')
else:
    print('老年人！')


# 尝试引发异常
# 尝试引发异常
try:
    raise IndexError
except KeyError:
    print('in KeyError except')
except IndexError:
    print('in IndexError except')
else:
    print('no exception')


# 单纯遍历的for语句
names = ['Michael', 'Bob', 'Tracy']
# 遍历输出names中的元素
for name in names:
    print(name)
 
    
# 第一层循环，遍历次数为4
for i in range(4):
    if i == 3:
        break
    print("-----%d-----" % i)
# 第二层循环，遍历次数为5
    for j in range(5):
        if j == 2:  # 当j等于2时，不执行操作
            pass
        elif j == 4:  # 当j等于4时，不执行循环
            continue
        else:
            print(j)
