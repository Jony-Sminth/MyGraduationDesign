import numpy as np
import functions
import gradient


class simpleNet:
    def __init__(self):
        self.W = np.random.randn(2, 3)

    def predict(self, x):
        return np.dot(x, self.W)

    def loss(self, x, t):
        z = self.predict(x)
        y = functions.softmax(z)
        loss = functions.cross_entropy_error(y, t)
        return loss


net = simpleNet()
print(net.W)  # 查看权重
x = np.array([0.6, 0.9])
t = np.array([0, 0, 1])  # 正确解
f = lambda w: net.loss(x, t)
dW = gradient.numerical_gradient_2d(f, net.W)
print(dW)
