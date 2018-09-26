
# coding: utf-8

# In[103]:

import math
import numpy as np


# In[104]:

def b_coef(n, k):
    if k > n / 2:
        return binomial_coefficient(n, n - k)
    result = 1
    for i in range(k):
        result *= (n - i) / (i + 1)
    return int(result)


# In[105]:

def create_points_Bezier(control_xs, control_ys, step):
    dot_num = len(control_xs)
    result_xs = []
    result_ys = []
    t = 0
    while t <= 1: 
        x, y = 0, 0
        for i in range(dot_num):
            coeff = b_coef(dot_num - 1, i) * t ** i * (1 - t) ** (dot_num - 1 - i)
            x += coeff * control_xs[i]
            y += coeff * control_ys[i]
        result_xs.append(x)
        result_ys.append(y)
        t += step
    return result_xs, result_ys


# In[106]:


def generate_polygon_dots(vertices_count, x_centre, y_centre, radius, startAngle = 0):
    xs = [x_centre + radius * math.cos(startAngle + 2 * math.pi * i / vertices_count) for i in range(vertices_count)]
    ys = [y_centre + radius * math.sin(startAngle + 2 * math.pi * i / vertices_count) for i in range(vertices_count)]
    return xs, ys


# In[107]:

points_num = 21
radius = 3
xs, ys = generate_polygon_dots (points_num,0,0, radius)
x_reflection_center=(xs[0]+xs[1])/2
y_reflection_center=(ys[0]+ys[1])/2
xs.append(xs[0]);
ys.append(ys[0]);
xs.append(xs[1]);
ys.append(ys[1]);
for i in range (points_num-2):
    xs.append(2*x_reflection_center-xs[vertices_count-i-1]);
    ys.append(2*y_reflection_center-ys[vertices_count-i-1]);
xs.append(xs[0]);
ys.append(ys[0]);
xs.append(xs[1]);
ys.append(ys[1]);
bezier_xs, bezier_ys = create_points_Bezier(xs, ys, 0.01)


# In[108]:

from matplotlib import pyplot
fig = pyplot.figure()
ax = fig.add_subplot(111)
polygon, = ax.plot(xs, ys, color='blue', alpha=0.7,
    linewidth=3, solid_capstyle='round', zorder=2, label='Input')
bezier, = ax.plot(bezier_xs, bezier_ys, color='red', alpha=0.7,
    linewidth=3, solid_capstyle='round', zorder=2, label='Bezier output')
pyplot.legend(handles=[polygon, bezier])
pyplot.show()


# In[ ]:




# In[ ]:



