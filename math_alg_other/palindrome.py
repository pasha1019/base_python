# Определение полиндрома через кортеж
print('Введите слово')
text = input()
palindrome = bool(text.find(text[::-1]) + 1)
if palindrome is True:
    print('Введенное слово полиндром')
else:
    print('Введенное слово не полиндром')
