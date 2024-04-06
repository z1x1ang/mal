import matplotlib.pyplot as plt
import numpy as np

# 起点和终点
s = (0, 0)
g = (10, 10)

# 创建一个图形和一个子图
fig, ax = plt.subplots()

# 绘制直线路径
ax.plot([s[0], g[0]], [s[1], g[1]], label='Straight Line')

# 绘制曲线路径
t = np.linspace(0, 1, 100)
x = (1 - t) * s[0] + t * g[0] + 5 * np.sin(2 * np.pi * t)
y = (1 - t) * s[1] + t * g[1] + 5 * np.cos(2 * np.pi * t)
ax.plot(x, y, label='Curved Path')

# 添加图例
ax.legend()

# 显示图形
plt.show()
