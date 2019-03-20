__author__ = 'Корнейчук Александр Николаевич'

# Задача-1: Дано произвольное целое число (число заранее неизвестно).
# Вывести поочередно цифры исходного числа (порядок вывода цифр неважен).
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании решите задачу с применением цикла for. 

number = int(input("Пожалуйста введите число: "))
while number > 0:
    n = number % 10
    print(n)
    number = number // 10

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Подсказка:
# * постарайтесь сделать решение через дополнительную переменную
#   или через арифметические действия
# Не нужно решать задачу так:
# print("a = ", b, "b = ", a) - это неправильное решение!

name = input("Введите свое имя: ")
lastName = input("Введите свою фамилию: ")
user = lastName + " " + name
print("Добро пожаловать ", user, "!")

# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"

age = int(input("Сколько Вам полных лет? "))

if age >= 18:
    print("Хорошо, вам ", age, " лет, доступ разрешен")
else:
    print("Доступ запрещен.")
