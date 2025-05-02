import random


array = []
for i in range(10):
    array.append(random.randint(1,9))
print(array)


def bubble_sort(massive):
    swap = False
    for i in range(len(massive) - 1, 0, -1):
        for j in range(i):
            if massive[j] > massive[j + 1]:
                massive[j], massive[j + 1] = massive[j + 1], massive[j]
                swap = True
        if swap:
            swap = False
        else:
            break
    return massive


print(bubble_sort(array))
