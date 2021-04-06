def exponent(a, b):
    x = a ** b
    return x

print('自定义幂运算的返回值为：', exponent(3, 6))


# 定义含有不同类型参数的自定义函数
def func(a, b=1, *numbers, **kwargs):
    print(a, b, numbers, kwargs)


print(func(2))
print(func(4, 2, 3, 4, c=2, d=3))


f = lambda x: x**2
print('50的平方为：', f(50))


f1 = lambda x: '传入的参数为1' if x == 1 else '传入的参数不为1'
print(f1(10))
