# Подсчет сумму первых n натуральных чисел с помощью рекурсии


def recursive(num):
    if num == 1:
        return num
    else:
        return num + recursive(num-1)


while True:
    try:
        print("Введите количество натуральных чисел для подсчета суммы")
        n = input()
        n = int(n)
        if n > 0:
            print(f"Cумма первых {n} натуральных чисел это {recursive(n)}")
            break
        else:
            raise Exception
    except ValueError:
        print('Неверный формат')
    except Exception:
        print('Введите число более 1')
