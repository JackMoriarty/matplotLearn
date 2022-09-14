import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 50)
y1 = 2*x+1

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
# x 轴在y=-1处
ax.spines['bottom'].set_position(('data', 0))
# y轴在x=0处
ax.spines['left'].set_position(('data', 0))

plt.plot(x, y1, label='up')

# 注解
x0 = 1
y0 = 2*x0 + 1
# 打印点
plt.scatter(x0, y0, s=50, color='blue')
plt.plot([x0, x0], [y0, 0], 'k--', linewidth=2.5) # 竖直虚线

# method 1
plt.annotate(r'$2x+1=%s$' % y0, xy=(x0, y0), xycoords='data', xytext=(+30, -30), textcoords='offset points',
    fontsize = 16, arrowprops=dict(arrowstyle='->', connectionstyle='arc3, rad=.2'))

#method 2
plt.text(-3.7, 3, r'$This\ is\ the\ the\ some\ text.\ \mu\ \sigma_i\ \alpha_t$', fontdict={'size':16, 'color':'r'})
plt.show()
