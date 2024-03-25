import numpy as np
import functions
import gradient

x = np.array([0.6, 0.9])
t = np.array([0, 0, 1])
W = np.random.randn(2, 3)
y = np.dot(x, W)
print(y)
y_sm = functions.softmax(y)
print(y_sm)
loss = functions.cross_entropy_error(y_sm, t)
print("损失", loss)
f = lambda W: functions.cross_entropy_error(y_sm, t)
print(f(W))
print(f(1))
dW = gradient.numerical_gradient_2d(f,W)
print(dW)