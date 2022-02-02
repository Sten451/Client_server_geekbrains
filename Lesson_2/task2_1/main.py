"""
1. Задание на закрепление знаний по модулю CSV. Написать скрипт,
осуществляющий выборку определенных данных из файлов info_1.txt, info_2.txt,
info_3.txt и формирующий новый «отчетный» файл в формате CSV.

Для этого:

Создать функцию get_data(), в которой в цикле осуществляется перебор файлов
с данными, их открытие и считывание данных. В этой функции из считанных данных
необходимо с помощью регулярных выражений или другого инструмента извлечь значения параметров
«Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
Значения каждого параметра поместить в соответствующий список. Должно
получиться четыре списка — например, os_prod_list, os_name_list,
os_code_list, os_type_list. В этой же функции создать главный список
для хранения данных отчета — например, main_data — и поместить в него
названия столбцов отчета в виде списка: «Изготовитель системы»,
«Название ОС», «Код продукта», «Тип системы». Значения для этих
столбцов также оформить в виде списка и поместить в файл main_data
(также для каждого файла);

Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл.
В этой функции реализовать получение данных через вызов функции get_data(),
а также сохранение подготовленных данных в соответствующий CSV-файл;

Пример того, что должно получиться:

Изготовитель системы,Название ОС,Код продукта,Тип системы

1,LENOVO,Windows 7,00971-OEM-1982661-00231,x64-based

2,ACER,Windows 10,00971-OEM-1982661-00231,x64-based

3,DELL,Windows 8.1,00971-OEM-1982661-00231,x86-based

Обязательно проверьте, что у вас получается примерно то же самое.

ПРОШУ ВАС НЕ УДАЛЯТЬ СЛУЖЕБНЫЕ ФАЙЛЫ TXT И ИТОГОВЫЙ ФАЙЛ CSV!!!
"""
import csv

def find_slice(find_slice_value):
    begin = find_slice_value.find(":")
    return (find_slice_value[begin + 1:]).strip()

def get_data(source_files):
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []
    main_data = ['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']

    for i in source_files:
        with open(i, mode='r', encoding='utf-8') as file:
            lines = file.readlines()
            for line in lines:
                if 'Изготовитель системы' in line or 'Название ОС' in line or 'Код продукта' in line or 'Тип системы' in line:
                    if 'Изготовитель системы' in line:
                        os_prod_list.append(find_slice(line))

                    if 'Название ОС' in line:
                        os_name_list.append(find_slice(line))

                    if 'Код продукта' in line:
                        os_code_list.append(find_slice(line))

                    if 'Тип системы' in line:
                        os_type_list.append(find_slice(line))

    main_data2 = [os_prod_list, os_name_list, os_code_list, os_type_list]
    main_data3 = []
    main_data4 = []
    # здесь формируем списки в главном списке при этом делая выборку по одинаковому индексу в каждом из исходных списков
    for s in range(len(main_data2) - 1):
        # вставка нумерации
        main_data3.append(s + 1)
        for i in main_data2:
            main_data3.append(i[s])
        main_data4.append(main_data3[:])
        main_data3.clear()
    del main_data2, main_data3, os_prod_list, os_name_list, os_code_list, os_type_list, line, lines
    return main_data, main_data4

def write_to_csv(url, source_files):
    res = get_data(source_files)
    print(res[1])
    with open(url, 'w', encoding='utf-8', newline='') as f:
        f_writer = csv.writer(f)
        f_writer.writerow(res[0])
        f_writer.writerows(res[1])

write_to_csv('final.csv', ['info_1.txt', 'info_2.txt', 'info_3.txt'])


