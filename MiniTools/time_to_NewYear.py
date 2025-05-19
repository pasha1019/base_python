import datetime


now_date = datetime.datetime.today()
new_year = now_date.year + 1
new_year_day = datetime.datetime(new_year, 1, 1)
date_X = new_year_day - now_date
minute, sec = divmod(date_X.seconds, 60)
hour, minute = divmod(minute, 60)

print("До нового года осталось:")
print(str(date_X.days) + ' ' + 'дней')
print(str(hour) + ' ' + 'часов')
print(str(minute) + ' ' + 'минут')
print(str(sec) + ' ' + 'секунд')

