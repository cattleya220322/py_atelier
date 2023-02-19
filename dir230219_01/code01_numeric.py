import numpy as np
import matplotlib.pyplot as plt

N = 60
dt = 0.1
x_init = 20
t = [0]
x = [x_init]


def T(n): return dt + t[n-1]


def X(n): return x[n-1] + dt * (-x[n-1])


for n in range(N):
    t.append(T(n+1))
for n in range(N):
    x.append(X(n+1))

plt.plot(t, x)

point = 100
xmin = 0
xmax = dt * N
x_exp = np.linspace(xmin, xmax, point)
y_exp = 20 * np.exp(-x_exp)
plt.plot(x_exp, y_exp)

plt.show()
