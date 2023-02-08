"""
1) Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

my_file = open('myfile.txt', 'w', encoding='utf-8')
line = input('Введите текст \n')

while len(line) > 0:
    my_file.writelines(f'{line}\n')
    line = input('Введите текст \n')
else:
    my_file.close()
