"""
Задание 5.

Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.

Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!!
"""
import subprocess
import chardet

def lesson_4 (ping):
    subproc_ping = subprocess.Popen(ping, stdout=subprocess.PIPE)

    for i in subproc_ping.stdout:
        type = chardet.detect(i)
        line = i.decode(type['encoding'])
        print(line)


lesson_4(['ping', 'yandex.ru'])
lesson_4(['ping', 'youtube.com'])