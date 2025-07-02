while True:
    print('Введите стороны треугольника')
    a = input()
    b = input()
    c = input()
    # Преобразование типа данных
    a = int(a)
    b = int(b)
    c = int(c)
    # Проверка на ввод числа < 0
    if a and b and c > 0:
        # Проверка на треугольник
        if ((a + b) > c) and ((a + c) > b) and ((b + c) > a):
            break
        else:
            print('Введите корректное значение')
# Проверка на тип треугольника
if (a == b) and (a == c):
    print('Треугольник равносторонний')
elif ((a == b) and (a != c)) or ((b == c) and (b != a)) or ((a == c) and (a != b)):
    print('Треугольник равнобедренный')
else:
    print('Треугольник разносторонний')
