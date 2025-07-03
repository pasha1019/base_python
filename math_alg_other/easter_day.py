# Расчет даты Пасхи
import datetime


print('Введите год для расчета')
year = input()
year = int(year)

a = year % 19

b = year % 4

c = year % 7

d = (19 * a + 15) % 30

e = (2 * b + 4 * c + 6 * d + 6) % 7

f = d + e
if f <= 26:
    h = datetime.date(year, 4, 4 + f)
else:
    h = datetime.date(year, 5, 26 - f)
print(f'ПАСХА  - {h}')
