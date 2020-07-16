import numpy as np

# 1、假设一个初始的数据和随机的权重
w = [2,-3,-3]
x = [-1, -2]
y = 1

# 2、前向传播计算
z = w[0]*x[0] + w[1]*x[1] + w[2]
a = 1.0 / (1 + np.exp(-z))
cost = -np.sum(y * np.log(a) + (1 - y) * np.log(1 - a))

print(cost)
# 3、反向梯度计算
dz = a - y
dw = [x[0] * dz, x[1] * dz, 1.0 * dz]

# 权重的梯度（在-1, -2这个点位置）
print(dw)