import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体为 SimHei
plt.rcParams['axes.unicode_minus'] = False    # 解决负号显示为方框的问题

x = np.linspace(0,10,50)# 生成一个数组，从 0 到 10，平均分成 50 个点
y1 = np.sin(x)
y2 = np.cos(x)

plt.figure(figsize=(8, 4))
plt.plot(x, y1, label="sin(x)", color="b")
plt.plot(x, y2, label="cos(x)", color="r", linestyle="--")
plt.legend()
plt.title("正弦和余弦函数")
plt.xlabel("x 值")
plt.ylabel("y 值")
plt.show()

# 散点图scatter
x_scatter = np.random.rand(50) * 10# random随机数模块，rand随机生成0到1的50个数并*10
y_scatter = np.random.rand(50) * 10
plt.scatter(x_scatter, y_scatter, color="g", alpha=0.6)
plt.title("随机散点图")
plt.show()

# 直方图
data = np.random.randn(1000)# randn随机生成1000个满足标准正态分布的数
plt.hist(data, bins=30, color="c", edgecolor="k", alpha=0.7)# edgecolor="k"：柱子边缘是黑色（k 是 black 的缩写）
plt.title("数据分布直方图")
plt.show()