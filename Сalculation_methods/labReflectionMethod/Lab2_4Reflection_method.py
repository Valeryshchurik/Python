
# coding: utf-8

# Щурик Валерий, ПИ-13

# #### Задание 4. Метод отражений
# 1. Используя библиотеку NumPy, написать программу, которая решает СЛАУ $Ax=b$ и вычисляет определитель матрицы $A$ методом отражений. Применить программу к следующим ниже входным данным и вывести результат.
# $$A=\left(
# \begin{array}{ccccccc}
#  -1 & -4 & -5 & -1 & 0 & -1 & -1 \\
#  -1 & -4 & 0 & 4 & -4 & 0 & -4 \\
#  -2 & -8 & -5 & -1 & 0 & -4 & 0 \\
#  -4 & -16 & -10 & 2 & -4 & -2 & 0 \\
#  -8 & -32 & -20 & 4 & -8 & 0 & -2 \\
#  -16 & -64 & -40 & 8 & -16 & -7 & -4 \\
#  5 & -5 & -5 & -2 & 0 & -2 & -1 \\
# \end{array}
# \right), \quad b = \left(
# \begin{array}{c}
#  -12 \\
#  -8 \\
#  -18 \\
#  -30 \\
#  -58 \\
#  -123 \\
#  -15 \\
# \end{array}
# \right)$$
# $$A = \left(
# \begin{array}{cccccccccc}
#  1 & 1 & 1 & 1 & 1 & 1 & 1 & 1 & 1 & 1 \\
#  1 & 2 & 4 & 8 & 16 & 32 & 64 & 128 & 256 & 512 \\
#  1 & 3 & 9 & 27 & 81 & 243 & 729 & 2187 & 6561 & 19683 \\
#  1 & 4 & 16 & 64 & 256 & 1024 & 4096 & 16384 & 65536 & 262144 \\
#  1 & 5 & 25 & 125 & 625 & 3125 & 15625 & 78125 & 390625 & 1953125 \\
#  1 & 6 & 36 & 216 & 1296 & 7776 & 46656 & 279936 & 1679616 &
#    10077696 \\
#  1 & 7 & 49 & 343 & 2401 & 16807 & 117649 & 823543 & 5764801 &
#    40353607 \\
#  1 & 8 & 64 & 512 & 4096 & 32768 & 262144 & 2097152 & 16777216 &
#    134217728 \\
#  1 & 9 & 81 & 729 & 6561 & 59049 & 531441 & 4782969 & 43046721 &
#    387420489 \\
#  1 & 10 & 100 & 1000 & 10000 & 100000 & 1000000 & 10000000 &
#    100000000 & 1000000000 \\
# \end{array}
# \right) 
# \quad
# b =\left(
# \begin{array}{c}
#  10 \\
#  1023 \\
#  29524 \\
#  349525 \\
#  2441406 \\
#  12093235 \\
#  47079208 \\
#  153391689 \\
#  435848050 \\
#  1111111111 \\
# \end{array}
# \right)
# $$
# $$A=\left(
# \begin{array}{cccccccccc}
#  5 & 3 & 3 & -4 & 5 & -5 & -4 & -5 & 0 & 2 \\
#  5 & 3 & -1 & 2 & 3 & 0 & -4 & 1 & -4 & -5 \\
#  10 & 6 & 2 & -3 & -2 & -2 & -1 & 0 & -3 & -5 \\
#  20 & 12 & 4 & -5 & -1 & -4 & 4 & -2 & -2 & -4 \\
#  40 & 24 & 8 & -10 & 5 & -1 & 5 & 2 & 0 & -3 \\
#  80 & 48 & 16 & -20 & 10 & -12 & -3 & -3 & 3 & 2 \\
#  160 & 96 & 32 & -40 & 20 & -24 & -3 & -4 & 1 & 4 \\
#  320 & 192 & 64 & -80 & 40 & -48 & -6 & -11 & 0 & -3 \\
#  640 & 384 & 128 & -160 & 80 & -96 & -12 & -22 & -5 & 2 \\
#  -3 & -3 & 0 & 0 & 5 & 3 & -2 & 2 & 5 & -2 \\
# \end{array}
# \right)
# \quad b =\left(
# \begin{array}{c}
#  -18 \\
#  2 \\
#  -8 \\
#  -6 \\
#  24 \\
#  30 \\
#  64 \\
#  100 \\
#  216 \\
#  0 \\
# \end{array}
# \right)$$
# 
# 2. Найти точное решение указанных систем с использованием  библиотеки SymPy и сравнить результаты.
# 
# 2. Вычислить число обусловленности в максимум-норме матрицы A из второго тестового задания. Что это означает на практике? Путем решения нескольких СЛАУ с возмущенным вектором b подтвердите связь между числом обусловленности и относительными погрешностями начальных данных и решения.
# 
# 3. Используя функцию `scipy.linalg.qr`, проведите экспериментальное исследование скорости построения QR-разложения в зависимости от размерности системы, используя для тестов матрицу $A$ со случайными коэффициентами. Постройте график зависимости времени работы от размерности. Задачу какой размерности ваша программа на вашем компьютере может решить за одну минуту?
# 

# In[1]:

#Примечание. Пусть А - матрица или вектор. Тогда обозначение вида A(T) следует читать
#как A транспонированное
import numpy as np
import sympy as sp

sp.init_printing()

matrix1 = [[-1, -4 , -5 , -1 , 0 , -1 , -1],
           [-1 , -4 , 0 , 4 , -4 , 0 , -4],
           [-2 , -8 , -5 , -1 , 0 , -4 , 0],
           [-4 , -16 , -10 , 2 , -4 , -2 , 0],
           [-8 , -32 , -20 , 4 , -8 , 0 , -2],
           [ -16 , -64 , -40 , 8 , -16 , -7 , -4],
           [5 , -5 , -5 , -2 , 0 , -2 , -1]]
b1 = [[-12],
 [-8],
 [-18],
 [-30],
 [-58],
 [-123],
 [-15]]


matrix2 = [[1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1],
 [1 , 2 , 4 , 8 , 16 , 32 , 64 , 128 , 256 , 512 ],
 [1 , 3 , 9 , 27 , 81 , 243 , 729 , 2187 , 6561 , 19683 ],
 [1 , 4 , 16 , 64 , 256 , 1024 , 4096 , 16384 , 65536 , 262144 ],
 [1 , 5 , 25 , 125 , 625 , 3125 , 15625 , 78125 , 390625 , 1953125 ],
 [1 , 6 , 36 , 216 , 1296 , 7776 , 46656 , 279936 , 1679616 , 10077696 ],
 [1 , 7 , 49 , 343 , 2401 , 16807 , 117649 , 823543 , 5764801 , 40353607 ],
 [1 , 8 , 64 , 512 , 4096 , 32768 , 262144 , 2097152 , 16777216 , 134217728 ],
 [1 , 9 , 81 , 729 , 6561 , 59049 , 531441 , 4782969 , 43046721 ,  387420489 ],
 [1 , 10 , 100 , 1000 , 10000 , 100000 , 1000000 , 10000000 , 100000000 , 1000000000 ]]
b2 =[[10], 
 [1023 ],
 [29524],
 [349525],
 [2441406],
 [12093235],
 [47079208],
 [153391689],
 [435848050],
 [1111111111]]

matrix3 = [[5 , 3 , 3 , -4 , 5 , -5 , -4 , -5 , 0 , 2 ],
 [5 , 3 , -1 , 2 , 3 , 0 , -4 , 1 , -4 , -5 ],
 [10 , 6 , 2 , -3 , -2 , -2 , -1 , 0 , -3 , -5],
 [20 , 12 , 4 , -5 , -1 , -4 , 4 , -2 , -2 , -4],
 [40 , 24 , 8 , -10 , 5 , -1 , 5 , 2 , 0 , -3 ],
 [80 , 48 , 16 , -20 , 10 , -12 , -3 , -3 , 3 , 2 ],
 [160 , 96 , 32 , -40 , 20 , -24 , -3 , -4 , 1 , 4 ],
 [320 , 192 , 64 , -80 , 40 , -48 , -6 , -11 , 0 , -3 ],
 [640 , 384 , 128 , -160 , 80 , -96 , -12 , -22 , -5 , 2 ],
 [-3 , -3 , 0 , 0 , 5 , 3 , -2 , 2 , 5 , -2 ]]
b3 =[[ -18 ],
 [2 ],
 [-8 ],
 [-6 ],
 [24 ],
 [30 ],
 [64 ],
 [100 ],
 [216 ],
 [0 ]]


# Задания 1, 2.

# In[2]:

def QRdecomp(A):

    (num_rows, num_cols) = np.shape(A)
    Q = np.identity(num_rows)
    R = np.copy(A)
    ''' Итак, наш алгоритм состоит m-1 итераций, где m-размерность матрицы
        на каждой итерации мы работаем с k-ым столбцом матрицы а
    '''
    for k in range(num_rows - 1):                                                                  
        # находим а_, у него все нули, кроме первого элемента, он представляет собой норму матрицы а с противоположным
        # диагональному элементу знаком. Можно было бы оставить и с тем же знаком, но
        # тогда возникли бы проблемы с вычитанием близких чисел
        a = R[k:,k]
        a_ = np.zeros_like(a)
        a_[0] = -np.sign(A[k, k])*np.linalg.norm(a)
        
        # находим вектор w
        u = a + a_ #вот здесь возникли бы проблемы, если бы мы взяли тот же знак
        w = u/np.linalg.norm(u)
        
        # Матрица Q_k представляет собой матрицу, которая является единичной до k-ых координат
        # дальше на главной диагонали лежит подматрица H_k, которая находится по формуле H_k=I-2w*w(T)
        # но мы не будем вводить H_k, а будем делать Q_k что называется "на месте"
        Q_k = np.identity(num_rows)
        Q_k[k:,k:] -=2.0*np.outer(w,w)
        # Домножаем наше Q_k на R слева, а Q на Q_k(T) справа
        R = np.dot(Q_k, R)
        Q = np.dot(Q, Q_k.T)
        # после последней итерации матрицы Q и R - это и будет результат нашего разложение
    return Q, R


# In[3]:

#методом Гаусса будем решать, когда уже получим R - треугольную матрицу
def gauss(A, b):
    x = np.linalg.solve(A,b)
    return x


# In[4]:

def QRsolve(A, b):
    Q, R = QRdecomp(A)
    # Имеем y=Q(T)b
    y = np.dot(np.linalg.inv(Q), b)
    # Далее решаем систему Rx=y Возвращаем первым параметром решение,
    # а вторым определитель, округленный до 3 знака после запятой
    return gauss(R, y), round(np.linalg.det(R), 3)


# In[5]:

def checkMyQRsolve(A, b):
    #Сравниваем наше решение со стандартом sympy и выводим определитель А
    x, det = QRsolve(np.matrix(A), np.matrix(b))
    print("det =", det)
    if det != 0:
        print("x =", x)
        print("\nreal_x =", (sp.Matrix(A)).QRsolve(sp.Matrix(b)))        


# In[6]:

checkMyQRsolve(matrix1, b1)


# Определитель равен нулю, поэтому у первой системы нет единственного решения.
# 

# In[7]:

checkMyQRsolve(matrix2, b2)


# In[8]:

checkMyQRsolve(matrix3, b3)


# Как видим, наши решения мало чем отличается от решений, найденных с помощью стандартных функций.

# In[9]:

Задание 3.


# In[10]:

"""число обусловленности невырожденной матрицы А равно ||А||*||А^(-1)||""" 
n = np.linalg.norm(np.matrix(matrix2), np.inf)
m_inv = np.linalg.inv(np.matrix(matrix2))
ch_ob = float(n*np.linalg.norm(m_inv, np.inf))
ch_ob


# In[11]:

#Интересно узнать, как такое большое число повлияет на ошибку в решении
b2_ = [[11], #изменили первую координату, она была равной 10
 [1023 ],
 [29524],
 [349525],
 [2441406],
 [12093235],
 [47079208],
 [153391689],
 [435848050],
 [1111111111]]
#погрешность начальных данных считается так: норма от 
#начального вектора - возмущенный делить на норму начального
b2_err = (sp.Matrix(b2) - sp.Matrix(b2_)).norm()/(sp.Matrix(b2)).norm()
print("Относительная погрешность начальных данных равна:")
float(b2_err)


# In[12]:

#погрешность решения считается аналогично
x2 = (sp.Matrix(matrix2)).QRsolve(sp.Matrix(b2))
x2_ = (sp.Matrix(matrix2)).QRsolve(sp.Matrix(b2_))
x2_err = (sp.Matrix(x2) - sp.Matrix(x2_)).norm()/(sp.Matrix(x2)).norm()
print("Относительная погрешность решения x2:")
float(x2_err)


# In[13]:

"""Видим, что относительная погрешность решения более, чем в 10 в 10-ой степени раз
превосходит погрешность начальных данных. Так как это связано с числоим обусловленности?
А вот как: число обучловленности больше либо равно относительной погрешности решания,
делённой на относительную погрешность условия."""
ch = x2_err/b2_err
if ch<ch_ob:
    print("true")
else:
    print("false")


# In[14]:

"""Поработаем теперь с третьей матрицей. Также найдем у нее число обусловленности и 
решив систему с возмущенным вектором рассмотрим погрешность решения.""" 
n2 = np.linalg.norm(np.matrix(matrix3), np.inf)
m_inv2 = np.linalg.inv(np.matrix(matrix3))
float(n2*np.linalg.norm(m_inv2, np.inf))


# In[15]:

b3_ = [[ -18 ],
 [2 ],
 [-8 ],
 [-6 ],
 [24 ],
 [30 ],
 [64 ],
 [100 ],
 [216 ],
 [0.000000208 ]] #я специально подобрал такое число, чтобы погрешность условия
#была примерно такой же, как и в предыдущей матрице

b3_err = (sp.Matrix(b3) - sp.Matrix(b3_)).norm()/(sp.Matrix(b3)).norm()
print("Относительная погрешность вектора b3:")
float(b3_err)


# In[16]:

x3 = (sp.Matrix(matrix3)).QRsolve(sp.Matrix(b3))
x3_ = (sp.Matrix(matrix3)).QRsolve(sp.Matrix(b3_))
x3_err = (sp.Matrix(x3) - sp.Matrix(x3_)).norm()/(sp.Matrix(x3)).norm()
print("Относительная погрешность решения x3:")
float(x3_err)


# In[17]:

ch3 = x3_err/b3_err
float(ch3)


# Итак число обусловленности третьей матрицы намного меньше, чем второй. Как это повлияло на практике? А вот как: при том, что относительные погрешности векторов b для второй и третьей матрицы почти одинаковы, колоссально отличаются погрешности в решениях. Для третьей матрицы погрешность ошибка в условии в нашем случае привела к 50-кратной ошибке в решении, хотя при другом возмущенном векторе в теории могла бы достичь до 156153-кратной ошибки а для второй матрицы мы получили при нашем возмущенном векторе ошибку 10-милииарднократную. При том, что в теории при другом возмщённом векторе могли бы получить еще в 330 раз большую ошибку. Таким образом число обусловленности определяет не только какую ошибку мы можем получить в общем случае, но и в целом тенденцию, что если число обусловленности одной матрицы больше, чем другой, то скорее всего и ошибка при решении слау с первой матрицей, будет больше, чем другой.

# # Task 4

# In[18]:

import numpy as np 
import time
import matplotlib.pyplot as plt
#итак будем раскладывать матрицу методом QR. Размерность от 10 до 2000 с шагом 10.
x = np.arange(10.0, 2000.0, 10)
y = np.zeros_like(x)
for i in range(10, 2000, 10):
    t_start = time.clock() 
    A = np.random.sample((i, i))
    np.linalg.qr(A)
    y[(int)(i/10) - 1] = time.clock() - t_start
    
fig = plt.figure()
plt.plot(x, y)
plt.ylabel('time for QR decomposition(sec)')
plt.xlabel('matrix size ')
plt.grid(True)

plt.show()


# In[19]:

print(y[99], "сек - время QR-разложения для матрицы размера", int(x[99]))


# In[20]:

#вычислительная сложность QR разложения O(n^(3))
#мы хотим узнать, какого же примерно размера матрицу наш компьютер сможет разложить за минуту
import math
p = 60.0/y[99]#во сколько раз увеличиваем время
n = p**(1/3)*x[99]
print("этот компьютер за минуту сможет разложить матрицу размера близкого к ", n)


# In[21]:

import numpy as np 
import time
import matplotlib.pyplot as plt
#итак будем раскладывать матрицу методом QR. Размерность от 10 до 2000 с шагом 10.
x = np.arange(10.0, 2000.0, 10)
y = np.zeros_like(x)
for i in range(10, 2000, 10):
    t_start = time.clock() 
    A = np.random.sample((i, i))
    np.linalg.qr(A)
    y[(int)(i/10) - 1] = time.clock() - t_start
    
fig = plt.figure()
plt.plot(x, y)
plt.ylabel('time for QR decomposition(sec)')
plt.xlabel('matrix size ')
plt.grid(True)

plt.show()


# Вообще главное преимущество QR разложения в том, что оно надёжное, так как не меняет число обусловленности в худшую сторону на этапе вычислений, так как число обусловленности ортогональной матрицы в спектральной норме равно 1

# In[ ]:



