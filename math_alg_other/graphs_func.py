# Построение графиков функций
from matplotlib import pyplot as plt
import numpy as np

print("Выберите тип элементарной функции \n"
       "1. Линейная (y = k * x + n)\n"
       "2. Гипербола (y =  k * (1 / x) + n)\n"
       "3. Парабола(y = k * x * x + n)\n"
       "4. Кубическая парабола (y = k * x * x * x + n)\n")
type_func = input()
array_X = []
array_Y = []
print("Введите параметры:")
print('k:\n')
k = int(input())
print('n:\n')
n = int(input())
if int(type_func) == 1:
       for x in range(6):
              y = k * x + n
              array_X.append(x)
              array_Y.append(y)
elif int(type_func) == 2:
       for x in np.arange(-6, 6, 1):
              try:
                     y = k * (1 / x) + n
                     array_X.append(x)
                     array_Y.append(y)
              except ZeroDivisionError:
                     pass
elif int(type_func) == 3:
       for x in np.arange(-6, 6, 1):
              y = k * x**2 + n
              array_X.append(x)
              array_Y.append(y)
elif int(type_func) == 4:
       for x in np.arange(-6, 6, 1):
              y = k * x**3 + n
              array_X.append(x)
              array_Y.append(y)
else:
       print('Выберите тип функции, введя от 1 до 4')
plt.plot(array_X, array_Y)
plt.title("График")
plt.ylabel('Ось Y')
plt.xlabel('Ось X')
plt.show()
