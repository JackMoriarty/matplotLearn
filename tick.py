# 坐标轴数值被挡住

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 50)
y1 = 0.1*x

# fig 1
plt.figure()

# 坐标轴取值范围
plt.xlim((-5,5))
plt.ylim((-2,5))

# 坐标轴label
plt.xlabel('I am x')
plt.ylabel('I am y')

# 移动坐标轴
ax = plt.gca()
# 右边和上边轴移除
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# 设定左边轴为y轴, 下边轴为x轴
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

# 移动x和y轴位置
# x 轴在y=0处
ax.spines['bottom'].set_position(('data', 0))
# y轴在x=0处
ax.spines['left'].set_position(('data', 0))

plt.plot(x, y1, linewidth=10, zorder=1)

for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontsize(12)
    label.set_bbox(dict(facecolor='white', edgecolor='None', alpha=0.7))
plt.show()
