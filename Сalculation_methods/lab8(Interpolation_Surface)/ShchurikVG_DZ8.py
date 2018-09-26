
# coding: utf-8

# In[33]:

import numpy as np
import math


# In[34]:

def Z(x, y):
    return 2.0 ** (x - y)


# In[35]:

def splineCFS(xs, zs):
    Interpolation_matrix = np.zeros((4 * (len(xs) - 1), 4 * (len(xs) - 1)))
    b_vector = np.zeros((4 * (len(xs) - 1)))
    size = len(xs) - 1
    for i in range(size):#условия для левых точек
        Interpolation_matrix[i, i * 4] = xs[i + 1] ** 3
        Interpolation_matrix[i, i * 4 + 1] = xs[i + 1] ** 2
        Interpolation_matrix[i, i * 4 + 2] = xs[i + 1]
        Interpolation_matrix[i, i * 4 + 3] = 1
        b_vector[i] = zs[i + 1]
    for i in range(size):#условия для правых точек
        Interpolation_matrix[size + i, i * 4] = xs[i] ** 3
        Interpolation_matrix[size + i, i * 4 + 1] = xs[i] ** 2
        Interpolation_matrix[size + i, i * 4 + 2] = xs[i]
        Interpolation_matrix[size + i, i * 4 + 3] = 1
        b_vector[size + i] = zs[i]
    for i in range(size - 1):#условия равенства первых производных
        Interpolation_matrix[2 * size + i, i * 4] = 3 * xs[i + 1] ** 2
        Interpolation_matrix[2 * size + i, i * 4 + 1] = 2 * xs[i + 1]
        Interpolation_matrix[2 * size + i, i * 4 + 2] = 1
        Interpolation_matrix[2 * size + i, (i + 1) * 4] = -3 * xs[i + 1] ** 2
        Interpolation_matrix[2 * size + i, (i + 1) * 4 + 1] = -2 * xs[i + 1]
        Interpolation_matrix[2 * size + i, (i + 1) * 4 + 2] = -1
        b_vector[2 * size + i] = 0
    for i in range(size - 1):#условия равенства вторых производных
        Interpolation_matrix[3 * size + i, i * 4] = 6 * xs[i + 1]
        Interpolation_matrix[3 * size + i, i * 4 + 1] = 2
        Interpolation_matrix[3 * size + i, (i + 1) * 4] = -6 * xs[i + 1]
        Interpolation_matrix[3 * size + i, (i + 1) * 4 + 1] = -2
    #недостающие начальные условия
    Interpolation_matrix[3 * size - 1, 0] = 6 * xs[0]
    Interpolation_matrix[3 * size - 1, 1] = 2
    Interpolation_matrix[-1, 0] = 6 * xs[-1]
    Interpolation_matrix[-1, 1] = 2
    return np.linalg.solve(Interpolation_matrix, b_vector)


# In[36]:

def make_cubical_spline(xs, zs):
    coeffs = splineCFS(xs, zs)
    def cubical_spline(x):
        if (x < xs[0] or x > xs[-1]):
            return None
        index = -1
        for i in range(len(xs) - 1):
            if (x < xs[i + 1]):
                index = i
                break
        return coeffs[4 * index] * x ** 3 + coeffs[4 * index + 1] * x ** 2 + coeffs[4 * index + 2] * x + coeffs[4 * index + 3]
    return cubical_spline


# In[37]:

def make_bicubical_spline(xs, ys, zs):
    spline_coeffs = []
    for j in range(len(ys)):
        spline_coeffs.append(splineCFS(xs, [zs[i][j] for i in range(len(xs))]))
    abcd_splines = [make_cubical_spline(ys, [spline_coeffs[i][j] for i in range(len(ys))]) for j in range(len(spline_coeffs[0]))]
    def bicubical_spline(x, y):
        if (x < xs[0] or x > xs[-1]):
            return None
        index = -1
        for i in range(len(xs) - 1):
            if (x < xs[i + 1]):
                index = i
                break
        return abcd_splines[4 * index](y) * x ** 3 + abcd_splines[4 * index + 1](y) * x ** 2 + abcd_splines[4 * index + 2](y) * x + abcd_splines[4 * index + 3](y)
    return bicubical_spline


# In[38]:

xs = [0, 0.1, 0.3, 0.6, 1]
ys = [0, 0.4, 0.7, 1]
zs = [[Z(xs[i], ys[j]) for j in range(len(ys))] for i in range(len(xs))]
bicubical_spline = make_bicubical_spline(xs, ys, zs)
zs_interp = [[bicubical_spline(xs[i], ys[j]) for j in range(len(ys))] for i in range(len(xs))]
for i in range(len(zs)):
    for j in range(len(zs[0])):
        print(zs[i][j], " ", zs_interp[i][j])


# In[39]:

plot_xs = [xs[0] + (xs[-1] - xs[0]) / 100 * i for i in range(101)]
plot_ys = [ys[0] + (ys[-1] - ys[0]) / 100 * i for i in range(101)]
plot_zs_func = [[Z(plot_xs[i], plot_ys[j]) for j in range(len(plot_ys))] for i in range(len(plot_xs))]
plot_zs_interp = [[bicubical_spline(plot_xs[i], plot_ys[j]) for j in range(len(plot_ys))] for i in range(len(plot_xs))]
file = open("BasicSurface.txt", "w+")
for i in range (len(plot_xs)):
    for j in range(len(plot_ys)):
        file.write(str(plot_xs[i]) + " " + str(plot_ys[j]) + " " + str(plot_zs_func[i][j]) + "\n")
file.close()
file = open("InterpolationSurface.txt", "w+")
for i in range (len(plot_xs)):
    for j in range(len(plot_ys)):
        file.write(str(plot_xs[i]) + " " + str(plot_ys[j]) + " " + str(plot_zs_interp[i][j]) + "\n")
file.close()


# In[ ]:



