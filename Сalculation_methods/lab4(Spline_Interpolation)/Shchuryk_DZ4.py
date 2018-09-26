
# coding: utf-8

# In[21]:

import numpy as np
import math
points=11
spline=4
R=(points-1)*(spline+1)


# In[22]:

M = np.zeros((R,R))
b = np.zeros(R)
Fx = np.zeros(points)
for i in range(points):
    x=i/2
    Fx[i]=math.cos(math.pi*x)
Fx


# In[23]:

for i in range(4*points-6,5*points-8):
    print(i)
    print((i-3*points+5)/2)


# In[24]:

for i in range(0,points-1):
    x=i/2
    for t in range (0,2):
        for s in range (0,5):
            M[2*i+t,s+5*i]=math.pow(x+t/2,4-s)
            b[2*i+t]=Fx[i+t]
b


# In[25]:

k=0
for i in range (2*points-2,3*points-4):
    x=(i-2*points+3)/2
    for t in range (0,2):
        if t==1:
            k+=1
        for s in range (0,4):
            M[i,s+5*k]=(4-s)*math.pow(x,3-s)*(2*t-1)
            b[i]=0
M


# In[26]:

k=0
for i in range (3*points-4,4*points-6):
    x=(i-2*points+3)/2
    for t in range (0,2):
        if t==1:
            k+=1
        for s in range (0,3):
            M[i,s+5*k]=(4-s)*(3-s)*math.pow(x,2-s)*(2*t-1)
            b[i]=0
M


# In[27]:

k=0
for i in range (4*points-6,5*points-8):
    x=(i-3*points+5)/2
    for t in range (0,2):
        if t==1:
            k+=1
        for s in range (0,2):
            M[i,s+5*k]=(4-s)*(3-s)*(2-s)*math.pow(x,1-s)*(2*t-1)
            b[i]=0
M


# In[28]:

x1=0
x2=-1*pow(math.pi,2)
x3=0
M[5*points-8,2]=2
M[5*points-7,1]=6
M[5*points-6,0]=24
b[5*points-8]=0
b[5*points-7]=-1*pow(math.pi,2)
b[5*points-6]=0
b


# In[29]:

S = np.linalg.solve(M, b)
S


# In[30]:

file = open('result.txt', 'w+')
file.write('Щурик Валерий Геннадьевич 3 курс 12 группа\n')
file.write('сплайны 4 порядка. Функция f(x) = cos(pi*x)\n')
g=0
for i in range (0,10):
    for j in range (0,5):
        g=(S[5*i+j])
        file.write(str(g)+'x^' + str(4-j) + ' + ')
    file.write('\n')


# In[31]:

def Podschet(a,b,c,d,e,X):
    return a*pow(X,4)+b*pow(X,3)+c*pow(X,2)+d*pow(X,1)+e


# In[34]:

import matplotlib.pyplot as plt
x=0
y=0
for t in range(0,10):
    for i in range (0,50):
        x=i/100+t/2
        y=Podschet(S[0+5*t],S[1+5*t],S[2+5*t],S[3+5*t],S[4+5*t],x)
        plt.plot(x, y, "black", marker="o", markerfacecolor="r")
        plt.plot(x, math.cos(math.pi*x),"blue", marker="o", markerfacecolor="b")
plt.show()


# In[ ]:



