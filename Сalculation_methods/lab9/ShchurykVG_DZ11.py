
# coding: utf-8

# In[37]:

import math
import time


# In[38]:

def f (x, u):
    return -u + math.cos(x) + math.sin(x)


# In[39]:

def next_u(prev_x, prev_y, h):
    k1=h*f(prev_x, prev_y)
    k2=h*f(prev_x+h/2, prev_y+k1/2)
    k3=h*f(prev_x+h, prev_y+2*k2-k1)
    next_y=prev_y+(k1+4*k2+k3)/6
    return next_y


# In[40]:

def get_steps():
    step = 15.0
    while True:
        yield step
        step /= 2.0


# In[41]:

x_first = 0
x_last = 30
u_first = 0
generator = get_steps()
elapsed = 0
while elapsed < 300:
    step = next(generator)
    start_time = time.clock()
    xs = [x_first + i * step for i in range (int(x_last / step + 1))]
    us = [u_first]
    for x in xs[1:]:
        us.append(next_u(x, us[-1], step))
    elapsed = time.clock() - start_time 
    print (step, '\t', us[len(xs) // 2] - math.sin((x_first + x_last) / 2), '\t', us[-1] - math.sin(x_last), '\t', elapsed)


# In[ ]:




# In[ ]:



