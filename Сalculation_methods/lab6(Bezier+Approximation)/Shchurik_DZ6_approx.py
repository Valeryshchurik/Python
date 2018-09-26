
# coding: utf-8

# In[80]:

import numpy as np
from scipy.linalg import solve
import random as rnd
import math


# In[81]:

def generateCirclePoints(num_points, h):
    x = [h * i for i in range(0, num_points)]
    y = [x[i] * random.uniform(0.9, 1.1) for i in range(0, num_points)]
    return x, y


# In[82]:

def generate_points(x_min, x_max, dot_count, deviation_min, deviation_max):
    step = (x_max - x_min) / dot_count
    xs = [x_min + i * step for i in range (dot_count)]
    ys = [math.sin(xs[i] ** 2) + rnd.uniform(deviation_min, deviation_max) for i in range (dot_count)]
    return xs, ys


# In[83]:

def countPhi(p, x, a = 1):
    return a * math.pow(x, p)


# In[84]:

def countBeta(i, ydata, xdata, num_points):
    b = 0
    for k in range(0, num_points):
        b += yinput[k] * countPhi(i, xinput[k])
    return b


# In[85]:

def countGamma(i, j, num_points):
    y = 0
    for k in range(0, num_points):
        y += countPhi(i, xinput[k]) * countPhi(j, xinput[k])
    return y


# In[86]:

def createEquations(xdata, ydata, N, num_points):
    matrix_a = np.zeros((N, N))
    vector_b = np.zeros(N)

    for l in range(0, N):
        vector_b[l] = countBeta(l, xinput, yinput, num_points)
        for i in range(0, N):
            matrix_a[l][i] = countGamma(i, l, num_points)

    return solve(matrix_a, vector_b)


# In[87]:

num_points = 100
N = 5
x_min, x_max = 0, 10
min_dx, max_dx = -0.1, 0.1
graph_points=1000
xinput, yinput = generate_points(x_min, x_max, num_points, min_dx, max_dx)
coefficients = createEquations(xinput, yinput, N, num_points)
xoutput, youtput = [],[]
for i in range (graph_points*x_max):
    x = i/graph_points
    xoutput.append(x)
    y = 0
    for j in range(0, N):
        y += countPhi(j, x, coefficients[j])
    youtput.append(y)


# In[88]:

from matplotlib import pyplot
fig = pyplot.figure()
ax = fig.add_subplot(111)
polygon, = ax.plot(xinput, yinput, color='blue', alpha=0.7,
    linewidth=3, solid_capstyle='round', zorder=2, label='Input')
bezier, = ax.plot(xoutput, youtput, color='red', alpha=0.7,
    linewidth=3, solid_capstyle='round', zorder=2, label='Approximation')
pyplot.legend(handles=[polygon, bezier])
pyplot.show()


# In[ ]:



