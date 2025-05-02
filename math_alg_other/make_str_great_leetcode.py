# Сложность: Лёгкая
# Условие задачи: дается строка, состоящая из латинских букв как в нижнем, так и в вернем регистре.
# Строка считается качественной, если две соседние буквы не представлены одной и той же буквой,
# но в разных регистрах. Такие буквы удаляются до тех пор, пока строка не станет качественной.
# Вернуть надо строку, над которой были совершены все преобразования. Гарантируется уникальность ответа.
# Пустая строка по умолчанию является качественной.
# Пример:
# Ввод: s = "leEeetcode"
# Вывод: "leetcode"
print('Введите строку')
new_str = input()
str_great = ''

for i in range(len(new_str)-1):
    if new_str[i].upper() == new_str[i+1]:
        if i == 0:
            str_great = new_str[2:]
        else:
            str_great = new_str[:i] + new_str[i + 2:]
        break

    elif new_str[i] == new_str[i+1].upper():
        if i == 0:
            str_great = new_str[2:]
        else:
            str_great = new_str[:i] + new_str[i + 2:]
        break
    else:
        str_great = new_str


print(str_great)
