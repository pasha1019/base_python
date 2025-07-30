# Представьте, что вы открыли в банке сберегательный счет под x % годовых. Проценты банк рассчитывает в конце года и добавляет к сумме счета.
# Напишите программу, которая запрашивает у пользователя сумму первоначального депозита, после чего рассчитывает и выводит на экран сумму
# на счету в конце i-го годов. Все суммы должны
# быть округлены до двух знаков после запятой.
while True:
    print('Введите сумму вклада')
    deposit = float(input())
    if deposit <= 0:
        print('Вы ввели неверное число')
    else:
        break
while True:
    print('Введите процент годовых')
    deposit_procent = int(input())
    if deposit_procent <= 0:
        print('Вы ввели неверное число')
    else:
        deposit_procent = deposit_procent/100
        break
while True:
    print('Введите срок вклада')
    time_deposit = int(input())
    if time_deposit <= 0:
        print('Вы ввели неверное число')
    else:
        break


sum_deposit = deposit
for i in range(1, time_deposit+1):
    sum_deposit += deposit*deposit_procent
    print(f'Сумма после {i} года = {format(sum_deposit,".2f")}')