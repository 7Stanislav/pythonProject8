"""
3) Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""

my_file = open('myfile2.txt', 'r', encoding='utf-8')
content = my_file.readlines()

count = 1
while count <= len(content):
    my_str = str(content[count - 1])
    a = my_str.replace("One", "Один").replace("Two", "Два").replace\
        ("Three", "Три").replace("Four", "Четыре")
    my_new_file = open('mynewfile.txt', 'a', encoding='utf-8')
    my_new_file.writelines(a)
    my_new_file.close()
    count += 1

my_file.close()
