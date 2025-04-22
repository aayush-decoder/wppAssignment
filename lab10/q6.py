import numpy as np
import matplotlib.pyplot as plt
import random

def func(x):
    return x**3 - 6*x**2 + 11*x - 6

while True:
    left = random.uniform(0, 2)
    right = random.uniform(2, 4)
    if func(left) * func(right) < 0:
        break

eps = 1e-6
tries = 100
history = []

for i in range(tries):
    mid = (left +right) / 2
    history.append(mid)
    if abs(func(mid)) < eps:
        break
    if func(left)*func(mid) < 0:
        right = mid
    else:
        left= mid

history = np.array(history)

x= np.linspace(0, 4, 400)
y= func(x)

plt.plot(x, y)
plt.axhline(0, color='gray', linestyle='--')
plt.scatter(history, func(history), color='red')

plt.grid()
plt.show()



