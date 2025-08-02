# Условие задачи: дается две строки needle и haystack,
# верните индекс первого появления иглы в стоге сена или -1, если игла не является частью стога сена.
# Пример:
# Ввод: haystack = "sadbutsad", needle = "sad"
# Вывод: 0
# Ввод: haystack = "leetcode", needle = "leeto"
# Вывод: -1
import timeit


x = 0
print('Введите стог сена')
haystack = input()
len_haystack = len(haystack)
print('Введите иглу')
needle = input()
len_needle = len(needle)

print('Первый способ')
start_time = timeit.default_timer()
for i in range(len_haystack):
    if haystack[i] == needle[0]:
        index = i
        if needle == haystack[index:index+len_needle:]:
            punch = 1
            print(index)
            break
        else:
            continue
if punch != 1:
    print('-1')
print(timeit.default_timer() - start_time)


print('Второй способ')
start_time = timeit.default_timer()
index = haystack.find(needle)
print(index)
print(timeit.default_timer() - start_time)