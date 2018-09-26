
# coding: utf-8

# In[7]:

import math
import time


# In[8]:

def function_derivative (x, u):
    return -u + math.cos(x) + math.sin(x)

def get_next_x_and_u(xu1, xu2, xu3):
    step = xu3[0] - xu2[0]
    while True:
        result = (xu3[0] + step, xu3[1] - step / 12*16 * function_derivative(xu2[0], xu2[1]) + 23 / 12 * step * function_derivative(xu3[0], xu3[1])+5 / 12 * step * function_derivative(xu1[0], xu1[1]))
        yield result
        xu1 = xu2
        xu2 = xu3
        xu3 = result

def get_steps():
    step = 15.0 / 8.0
    while True:
        yield step
        step /= 2.0


# In[9]:

step_generator = get_steps()
elapsed = 0
x_first = 0
x_last = 30
while elapsed < 300:
    step = next(step_generator)
    xu1 = (3 * step, math.sin(3 * step))
    xu2 = (4 * step, math.sin(4 * step))
    xu3 = (5 * step, math.sin(5 * step))
    xu_generator = get_next_x_and_u(xu1, xu2, xu3)
    result = (0.0, 0.0)
    eps15 = 0
    eps30 = 0
    start_time = time.clock()
    while result[0] < x_last:
        result = next(xu_generator)
        if (result[0] == x_last / 2):
            eps15 = result[1] - math.sin((x_first + x_last) / 2)
    eps30 = result[1] - math.sin(x_last)
    elapsed = time.clock() - start_time 
    print (step, '\t', eps15, '\t', eps30, '\t', elapsed)


# In[ ]:



