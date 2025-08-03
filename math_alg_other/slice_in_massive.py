# Условие задачи: дается массив из уникальных целых чисел цисел.
# Срез [a,b] - включает в себя множество значений из данного отрезка включительно.
# # Необходимо верноть наименьший отсортированный список диапазонов, покрывающих все в массиве.
# Это означает, что каждый элемент из исходного массива должен быть включен только в единственный диапазон,
# и нет такого элемнта из исходного массива, что этот элемент будет в одном из диапазонов,
# но будет остутствовать в исходном массиве.
# #  • "a->b" if a != b
#  • "a" if a == b
# # Пример:
# # Ввод: nums = [0,1,2,4,5,7]
# Вывод: ["0->2","4->5","7"]
import random


massive = []
new_massive = []
for x in range(5):
    x = random.randint(0, 10)
    if x not in massive:
        massive.append(x)
massive = sorted(massive)
print(massive)

def summary_range(nums):
    ranges = []
    for n in nums:
        if not ranges or n > ranges[-1][-1]+1:
            ranges += [],
        ranges[-1][1:] = n,
    return ['->'.join(map(str, r)) for r in ranges]

print(summary_range(massive))