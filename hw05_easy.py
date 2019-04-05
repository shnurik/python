
__author__ = 'Корнейчук Александр Николаевич'

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os
import shutil
import sys

path_dir = [('dir_' + str(i + 1)) for i in range(9)]


def make_dir(paths):
    dir_path = os.path.join(os.getcwd(), paths)
    try:
        os.mkdir(dir_path)
    except:
        print(dir_path + ' - такая директория уже есть')


for i in path_dir:
    make_dir(i)


def delete_dir(path_dir):
    try:
        os.rmdir(path_dir)
    except:
        print(path_dir + ' - такой директории нет')


for i in path_dir:
    delete_dir(i)

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.


def list_dir(main_path):
    for _ in os.listdir(main_path):
        print(_)


main_path = os.getcwd()


list_dir(main_path)


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.


def copy_file(first_file, backup_file):
    shutil.copy(first_file, backup_file)


first_file = sys.argv[0]
backup_file = first_file + '.backup'
copy_file(first_file, backup_file)

# Функция для normal


def change_dir(path_dir):
    try:
        os.chdir(path_dir)
        print(os.getcwd() + ' - текущая директория')
    except:
        print(path_dir + ' - такой директории нет')
