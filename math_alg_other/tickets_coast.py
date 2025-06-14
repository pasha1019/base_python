sum_age = 0
count_people = 0
ticket_price = 0
while True:
    print('Введите возраст посетителя')
    age = input()
    if age != '':
        age = int(age)
        if age <= 2:
            count_people += 1
            ticket_price += 0
        elif 2 < age <= 12:
            count_people += 1
            ticket_price += 14
        elif 12 < age <= 65:
            count_people += 1
            ticket_price += 23
        elif age > 65:
            count_people += 1
            ticket_price += 18
    else:
        print(f'Всего {count_people} посетителей на сумму {ticket_price} $')
        break