import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 50)
y1 = 2*x+1
y2 = x**2

# fig 1
plt.figure()

# 坐标轴取值范围
plt.xlim((-1,2))
plt.ylim((-2,3))

# 坐标轴label
plt.xlabel('I am x')
plt.ylabel('I am y')

# 坐标轴刻度设定
new_ticks = np.linspace(-1, 2, 5)
print(new_ticks)
plt.xticks(new_ticks)
plt.yticks([-2, -1.8, -1, 1.22, 3], 
            [r'$really\ bad$', r'$bad\ \alpha$', r'$normal$', 'good', 'really good'])
            # 数学形式

l1, = plt.plot(x, y2, label='up')
l2, = plt.plot(x, y1, color='red', linewidth=1.0, linestyle='--', label='down')
# 绘制图例, loc: best, upper right 等, labels用于指定图例名称, 也可在plot中指定
plt.legend(handles=[l1, l2,], labels=['aaa', 'bbb'], loc='best')

plt.show()