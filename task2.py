"""
2) Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

my_file = open('myfile1.txt', 'r', encoding='utf-8')
content = my_file.readlines()
print(content)
print(f'Количество строк: {len(content)}')

count = 1
while count <= len(content):
    my_str = str(content[count - 1])
    p = my_str.count(' ')
    print(f'Количество слов в {count} строке - {p + 1}')
    count += 1

my_file.close()
