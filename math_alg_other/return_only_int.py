# Напишите функцию, которая принимает список элементов и возвращает только целые числа
#
# Пример:
# return_only_integer([9, 2, "space", "car", "lion", 16]) ➞ [9, 2, 16]
user_list = []
print('Введите элементы')
while True:
    a = input()
    if a == ' ':
        break
    else:
        user_list.append(a)


def return_only_int(some_list):
    new_list = []
    for i in range(len(some_list)):
        try:
            x = int(some_list[i])
            new_list.append(x)
        except ValueError:
            pass
    print(new_list)


return_only_int(user_list)