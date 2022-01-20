"""
Задание 3.

Определить, какие из слов «attribute», «класс», «функция», «type»
невозможно записать в байтовом типе с помощью маркировки b'' (без encode decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
--- обязательно!!! усложните задачу, "отловив" и обработав исключение,
придумайте как это сделать
"""

for i in ['attribute', 'класс', 'функция', 'type']:
    try:
        bytes(i, encoding='ascii')
    except UnicodeEncodeError:
        print(f'Слово: "{i}" невозможно записать в байтовом виде')


