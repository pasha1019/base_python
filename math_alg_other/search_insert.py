# Сложность: Лёгкая
# Условие задачи: дается отсортированный массив различных целых чисел и целевое значение, верните индекс,
# если целевое значение найдено. Если нет, верните индекс туда, где он был бы, если бы он был вставлен по порядку.
# Вы должны написать алгоритм с O(log n) сложностью во время выполнения.
# Пример:
# Ввод: nums = [1,3,5,6], target = 5
# Вывод: 2
# Ввод:nums = [1,3,5,6], target = 2
# Вывод: 1
import random


nums = []
target = []


def search_index(num_of_massive, massive):
    index = 0
    for x in range(len(massive)):
        if num_of_massive == massive[x]:
            index = x
            break
    return index


for i in range(4):
    nums.append(random.randint(1, 9))
nums = sorted(nums)
print(nums)
print('Введите число от 1 до 9')
num_target = int(input())

if num_target in nums:
    print(search_index(num_target, nums))
else:
    nums.append(num_target)
    nums = sorted(nums)
    print(search_index(num_target, nums))
