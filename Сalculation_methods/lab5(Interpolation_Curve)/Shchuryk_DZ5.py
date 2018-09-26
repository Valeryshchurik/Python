
# coding: utf-8

# In[181]:

import numpy as np
import math
points=20
r=10


# In[182]:

t = np.zeros(points)
x = np.zeros(points)
y = np.zeros(points)
xout = np.zeros(points)
yout = np.zeros(points)
for i in range(points):
    t[i]=math.pi*2*i/(points)
    x[i]=r*math.cos(t[i])
    y[i]=r*math.sin(t[i])


# In[183]:

def Multiplier (i,j):
    return np.poly1d([1 / (t[i] - t[j]), -t[j] / (t[i] - t[j])])


# In[184]:

def Slagaemoe (coord_i, i):
    polynomial = np.poly1d([coord_i])
    for j in range(0, points):
        if j == i:
            continue
        polynomial = np.polymul(polynomial, Multiplier(i,j))
    return polynomial


# In[185]:

interpolation_polynomX=np.poly1d([0])
interpolation_polynomY=np.poly1d([0])
for i in range (0, points):
    interpolation_polynomX=np.polyadd(interpolation_polynomX, Slagaemoe (x[i], i))
    interpolation_polynomY=np.polyadd(interpolation_polynomY, Slagaemoe (y[i], i))
print(interpolation_polynomX)
print(interpolation_polynomY)


# In[ ]:




# In[186]:

import matplotlib.pyplot as plt
x=0
y=0
for t in range (0,1000):
    value=t/1000*math.pi*2
    x=np.polyval(interpolation_polynomX, value)
    y=np.polyval(interpolation_polynomY, value)
    plt.plot(x, y, "black", marker="o", markerfacecolor="r")
plt.show()

file = open('result.txt', 'w+')
file.write('Щурик Валерий Геннадьевич 3 курс 12 группа\n')
file.write('Интерполяция кривой. x=10*cos(t), y=10*sin(t)\n')
file.write('Вариант 1.Исходные точки распределены по окружности равномерно. Интерполируем по правилу "t - равномерное"\n')
file.write('По пока непонятным причинам, при количестве точек большем 20 под конец наша кривая куда-то улетает. Поэтому пока я оставил n=20"\n')
    
# In[ ]:



