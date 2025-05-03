# Определение палиндрома через кортеж
print('Введите слово')
text = input()
palindrome = bool(text.find(text[::-1]) + 1)
if palindrome is True:
    print('Введенное слово палиндром')
else:
    print('Введенное слово не палиндром')
