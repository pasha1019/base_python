# Условие задачи: дан массив arr из натуральных чисел,
# отсортированных в строго возрастающем порядке, и целое число k.
# Возвращает k-е положительное целое число, отсутствующее в этом массиве.
# # Пример:
# # Ввод: arr = [2,3,4,7,11], k = 5
# Вывод: 9
# # Ввод: arr = [1,2,3,4], k = 2
# Вывод: 6
i = 0
massive = []
missing = 0
print('Введите элемент массива')
while True:
    num = input()
    if num == ' ':
        break
    else:
        massive.append(int(num))
        i += 1
print('Введите K')
k = int(input())
massive = sorted(massive)
for x in range(1, 99):
    if x not in massive:
        missing += 1
        if missing == k:
            print(x)
        else:
            continue