import random


def BinSearch(a, i, num_search):
    first = 0
    last = i - 1
    index = -1
    while (first <= last):
        mid = (first + last) // 2
        if (a[mid] == num_search) and (index == -1):
           index = mid
        else:
            if num_search < a[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return index

a = []

print('Введите количество элементов')
i = int(input())
for x in range(0, i):
    a.append(random.randint(1, 99))
print(a)
a.sort()
print(a)
print('ОК. Введите элемент который нужно найти')
num_search = int(input())
print('Индекс элемента:', BinSearch(a, i, num_search))
