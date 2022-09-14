import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 50)
y1 = 2*x+1
y2 = x**2

# fig 1
plt.figure()
plt.plot(x, y2)
plt.plot(x, y1, color='red', linewidth=1.0, linestyle='--')

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


# gca = 'get current axis'
# 移动坐标轴
ax = plt.gca()
# 右边和上边轴移除
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# 设定左边轴为y轴, 下边轴为x轴
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

# 移动x和y轴位置
# x 轴在y=-1处
ax.spines['bottom'].set_position(('data', -1))
# y轴在x=0处
ax.spines['left'].set_position(('data', 0))

plt.show()