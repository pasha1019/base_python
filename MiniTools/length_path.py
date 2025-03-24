import os


max_length = 260
normal_path = 0
summary_files = 0
print('Введите имя каталога для проверки длины абсолютных путей:')
catalog_name = input()
for address, directions, files in os.walk(catalog_name):
    for name in files:
        path_file = os.path.join(address, name)
        length = len(path_file)
        if length <= max_length:
            normal_path += 1
            summary_files += 1
        else:
            f = open('long_path.txt', 'a+')
            f.write(path_file + '\n')
            f.close()
            summary_files += 1
if summary_files > normal_path:
    print('Есть файлы с слишком длинными абсолютными путями')
else:
    print('Все пути меньше или равны 260 символам')
