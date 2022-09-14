import matplotlib.pyplot as plt
import numpy as np

n = 12
a=np.arange(n)

# 均匀分布
b1 = (1-a/float(n)) * np.random.uniform(0.5, 1.0, n)
b2 = (1-a/float(n)) * np.random.uniform(0.5, 1.0, n)

plt.bar(a, b1, facecolor='#9999ff', edgecolor='white')
plt.bar(a, -b2, facecolor='#ff9999', edgecolor='white')

# 增加数字值
for x, y in zip(a, b1):
    # ha: horizontal alignment
    # va = vertical alignment
    plt.text(x, y+0.05, '%.2f' % y, ha='center', va='bottom')

for x, y in zip(a, b2):
    # ha: horizontal alignment
    # va = vertical alignment
    plt.text(x, -y-0.05, '-%.2f' % y, ha='center', va='top')
plt.show()