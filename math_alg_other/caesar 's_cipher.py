# Шифрование
print('Введите фразу для шифрования')
phrase = input()
print('Введите сдвиг')
x = int(input())
new_phrase = ''

for i in phrase:
    new_phrase += chr(ord(i) + x)
print(new_phrase)

# Дешифрование
print('Введите фразу для дешифрования')
phrase_2 = input()
print('Введите сдвиг')
y = int(input())
new_phrase_2 = ''
for i in phrase_2:
    new_phrase_2 += chr(ord(i) + y)
print(new_phrase_2)
