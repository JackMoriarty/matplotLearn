import matplotlib.pyplot as plt

plt.figure()

# 子图2行6列, 位置1绘制
plt.subplot(2, 1, 1)
plt.plot([0,1], [0,1])

# 子图2行6列, 位置4绘制
plt.subplot(2, 3, 4)
plt.plot([0,1], [0,1])

# 子图2行6列, 位置5绘制
plt.subplot(2, 3, 5)
plt.plot([0,1], [0,1])

# 子图2行6列, 位置6绘制
plt.subplot(2, 3, 6)
plt.plot([0,1], [0,1])

plt.show()