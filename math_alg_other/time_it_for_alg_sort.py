import random
import timeit


# Создание массива
x = []
for num in range(50):
    x.append(random.randint(1, 100))


# Сортировка 1
def base_sort(list_1):
    new_x = sorted(list_1)
    print(new_x)


# Сортировка 2
def sort_bubble(list_2):
    n = len(list_2)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if list_2[j] > list_2[j + 1]:
                list_2[j], list_2[j + 1] = list_2[j + 1], list_2[j]
    print(list_2)


start_time = timeit.default_timer()
base_sort(x)
print(timeit.default_timer() - start_time)


start_time = timeit.default_timer()
sort_bubble(x)
print(timeit.default_timer() - start_time)