# leetcode task


def sort_list(new_list):
    new_list2 = sorted(new_list)
    new_list3 = sorted(new_list, reverse=True)
    if new_list2 == new_list or new_list3 == new_list:
        return True
    else:
        return False


while True:
    print("Введите список")
    list_user = input()
    list_user = list(list_user)
    if len(list_user) == 1:
        print('Введите список из нескольких элементов')
    elif len(list_user) == 0:
        print('Вы ввели пустой список, введите список из нескольких элементов')
    else:
        break

if sort_list(list_user) is True:
    print('Список отсортирован')
else:
    print('Список не сортирован')
