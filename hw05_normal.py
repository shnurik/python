
__author__ = 'Корнейчук Александр Николаевич'

import os
import hw05_easy

answer = 'a'
while answer != '0':
    print('Перейти в папку - [1]')
    print('Просмотреть содержимое текущей папки - [2]')
    print('Удалить папку - [3]')
    print('Создать папку - [4]')
    print('для выхода - [0]')
    answer = input('Выбрать: ')
    print(answer)
    if answer == '1':
        dir_name = input('наберите полный путь папки: ')
        hw05_easy.change_dir(dir_name)
    elif answer == '2':
        dir_name = os.getcwd()
        hw05_easy.list_dir(dir_name)
    elif answer == '3':
        dir_name = input('наберите полный путь папки: ')
        hw05_easy.delete_dir(dir_name)
    elif answer == '4':
        dir_name = input('наберите полный путь папки: ')
        hw05_easy.make_dir(dir_name)
    elif answer == '0':
        pass
    else:
        print('Такого пункта меню нет')
