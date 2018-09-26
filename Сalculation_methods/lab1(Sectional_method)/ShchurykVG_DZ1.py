
# coding: utf-8

# In[99]:

import math, time


# In[100]:

def formula(x):

    res=math.tan(x)*math.log(x+1)+((math.e**x)**x)*x-(2**x)*x*x
    return res


# In[101]:

xk0 = 0.5
xk1 = 0.847326246762699
xk2 = 0
c=0
t0=time.time()
while (math.fabs(xk1)>1*(10**(-15))):
    xk2=xk1-(xk1-xk0)/(formula(xk1)-formula(xk0))*formula(xk1)
    xk0=xk1
    xk1=xk2
    c+=1
    print(xk1)
t=time.time()-t0
print ("Число итераций =", c, ". Выполнено за время ", t)


# In[ ]:



