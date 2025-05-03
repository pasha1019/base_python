import random


x = []
for i in range(20):
    x.append(random.randint(1, 100))
max_int = x[0]
izm = 0
for i in range(20):
    if x[i] > max_int:
        print(x[i], '  <<== Обновление')
        max_int = x[i]
        izm += 1
    else:
        print(x[i])
print(f'Максимальное число = {max_int}, а количество обновлений максимума = {izm}')
