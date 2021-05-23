# 代码 5-1
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(6, 6), dpi=80)  # 创建画布。大小为6×6，像素为80
x = np.linspace(0, 1, 1000)
fig.add_subplot(2, 1, 1)  # 分为2×1图形阵，选择第1张图片绘图
plt.title('y=x^2 & y=x')  # 添加标题
plt.xlabel('x')  # 添加x轴名称‘x’
plt.ylabel('y')  # 添加y轴名称‘y’
plt.xlim((0, 1))  # 指定x轴范围（0,1）
plt.ylim((0, 1))  # 指定y轴范围（0,1）
plt.xticks([0, 0.3, 0.6, 1])  # 设置x轴刻度
plt.yticks([0, 0.5, 1])  # 设置y轴刻度
plt.plot(x, x ** 2)
plt.plot(x, x)
plt.legend(['y=x^2', 'y=x'])  # 添加图例
plt.savefig('../tmp/整体流程绘图.png')  # 保存图片
plt.show()


# 代码 5-2
def my_plotter(ax, x, y, param_dict):
    '''
    ax 接收绘图对象
    x  接收array 表示横轴数据 无默认值
    y  接收array 表示纵轴数据 无默认值
    param_dict 接收dict 表示传入参数 无默认值
    '''
    out = ax.plot(x, y, **param_dict)
    return out


# 以如下方式使用函数
x = [0, 1, 2, 3, 4, 5, 6, 7, 8]
y1 = x
y2 = np.sin(x)
fig, (ax1, ax2) = plt.subplots(1, 2)
my_plotter(ax1, x, y1, {'marker': 'x'})
my_plotter(ax2, x, y2, {'marker': 'o'})
ax1.text(x[4], y1[4], 'y=x')  # 在子图1添加‘y=x’
ax2.text(x[4], y2[4], 'y=sin(x)')  # 在子图2添加‘y=sin（x）’
plt.savefig('../tmp/自编函数绘图并添加文本.png')
plt.show()

# 代码 5-3
print('Matplotlib中预设风格为：\n', plt.style.available)

x = np.linspace(0, 1, 1000)
plt.title('y=x^2 & y=x')  # 添加标题
plt.style.use('ggplot')  # 使用ggplot风格
plt.plot(x, x ** 2)
plt.plot(x, x)
plt.legend(['y=x^2', 'y=x'])  # 添加图例
plt.savefig('../tmp/plt风格.png')  # 保存图片
plt.show()

# 代码 5-4
import matplotlib as mpl

pic = plt.figure(dpi=80, figsize=(6, 6))
x = np.linspace(0, 1, 1000)

# 绘制第一张图（从左往右从上到下）
pic.add_subplot(2, 2, 1)  # 绘制2×2图形阵中第1张图片
plt.rcParams['lines.linestyle'] = '-.'  # 修改线条类型
plt.rcParams['lines.linewidth'] = 1  # 修改线条宽度
plt.plot(x, x ** 2)
plt.title('y = x^2')

# 绘制第二张图
pic.add_subplot(2, 2, 2)
# 以matplotlib.rc()函数命令方式修改rc参数
mpl.rc('lines', linestyle='--', linewidth=10)
plt.plot(x, x ** 2)
plt.title('y = x^2')

# 绘制第三张图
pic.add_subplot(2, 2, 3)
plt.rcParams['lines.marker'] = None  # 修改线条上点的形状
plt.rcParams['lines.linewidth'] = 3
plt.plot(x, x ** 2)
plt.title('y = x^2')

# 绘制第四张图
pic.add_subplot(2, 2, 4)
plt.rcParams['lines.linestyle'] = ':'
plt.rcParams['lines.linewidth'] = 6
plt.plot(x, x ** 2)
plt.title('y = x^2')
plt.savefig('../tmp/线条rc参数对比.png')
plt.show()

# 代码 5-5
x = np.linspace(0, 10, 1000)
plt.plot(x, np.sin(x))
plt.show()

x = np.linspace(0, 10, 1000)
plt.rcParams['axes.edgecolor'] = 'b'  # 轴颜色设置为蓝色
plt.rcParams['axes.grid'] = True  # 添加网格
plt.rcParams['axes.spines.top'] = False  # 去除顶部轴
plt.rcParams['axes.spines.right'] = False  # 去除右侧轴
plt.rcParams['axes.xmargin'] = 0.1  # x轴余留为区间长度的0.1倍
plt.plot(x, np.sin(x))
plt.show()

# 代码 5-6
# 原图
x = np.arange(0, 10, 0.2)
y = np.sin(x)
fig = plt.figure()
fig.add_subplot(111)
plt.title('sin曲线')
plt.plot(x, y)
plt.savefig('../tmp/sin曲线1.png')
plt.show()

# 修改参数后
plt.rcParams['font.sans-serif'] = 'SimHei'  # 设置字体为SimHei
plt.rcParams['axes.unicode_minus'] = False  # 解决负号“-”显示异常
plt.title('sin曲线')
plt.plot(x, y)
plt.savefig('../tmp/sin曲线2.png')
plt.show()
