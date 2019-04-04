
__author__ = 'Корнейчук Александр Николаевич'

import os
import hw05_easy

exitos = 'a'
while exitos != '0':
    print('Перейти в папку - выбрать 1')
    print('Просмотреть содержимое текущей папки - выбрать 2')
    print('Удалить папку - выбрать 3')
    print('Создать папку - выбрать 4')
    print('для выхода - выбрать 0')
    exitos = input('Выбрать: ' )
    print(exitos)
    if exitos == '1':
        dir_name = input ('наберите полный путь папки: ')
        hw05_easy.change_dir(dir_name)
    elif exitos == '2':
        dir_name = os.getcwd()
        hw05_easy.list_dir(dir_name)
    elif exitos == '3':
        dir_name = input('наберите полный путь папки: ')
        hw05_easy.delete_dir(dir_name)
    elif exitos == '4':
        dir_name = input('наберите полный путь папки: ')
        hw05_easy.make_dir(dir_name)
    elif exitos == '0':
        pass
    else:
        print('Такого пункта меню нет')