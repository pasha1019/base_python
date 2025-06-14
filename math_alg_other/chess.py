# Определение цвета клетки поля
print('Введите координаты клетки')
coord = input()
coord = list(coord)
# Проверка на имя поля
if coord[0] == 'a':
    index = 1
elif coord[0] == 'b':
    index = 2
elif coord[0] == 'c':
    index = 3
elif coord[0] == 'd':
    index = 4
elif coord[0] == 'e':
    index = 5
elif coord[0] == 'f':
    index = 6
elif coord[0] == 'g':
    index = 7
else:
    index = 8

# Вычисляем координату и проверяем

coord_chess = index * int(coord[1])
if (coord_chess % 2) == 1:
    print('Черное')
else:
    print('Белое')